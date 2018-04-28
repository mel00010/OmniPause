#!/usr/bin/env python2
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.



import dbus
import sys
import os
from dbus.mainloop.glib import DBusGMainLoop


directory = '/tmp/omniPause'
players   = []
DBusGMainLoop(set_as_default=True)
bus       = dbus.SessionBus()

def do_nothing(*args, **kwargs):
    pass

def get_player_name(i, player):
	if i.startswith("org.mpris.MediaPlayer2."):
		return i[len("org.mpris.MediaPlayer2."):]
	else:
		return player.Get('org.mpris.MediaPlayer2','DesktopEntry', dbus_interface='org.freedesktop.DBus.Properties')


def pause():
	player_names = []
	for i in players:
		player = bus.get_object(i, '/org/mpris/MediaPlayer2')
		player_status = player.Get('org.mpris.MediaPlayer2.Player','PlaybackStatus', dbus_interface='org.freedesktop.DBus.Properties')
		if player_status == 'Playing':
			player_name = get_player_name(i, player)
			player_names.append(player_name)
			player.Pause(dbus_interface='org.mpris.MediaPlayer2.Player', reply_handler=do_nothing, error_handler=do_nothing)

	if player_names != []:
		for i in os.listdir(directory+'/paused-players/'):
			os.remove(directory+'/paused-players/'+i)
		for player_name in player_names:
			player_status_file = open(directory+'/paused-players/'+player_name, "w")
			player_status_file.close()

def play():
	for i in os.listdir(directory+'/paused-players/'):
		try:
			player = bus.get_object('org.mpris.MediaPlayer2.'+i, '/org/mpris/MediaPlayer2')
		except:
			if i in os.listdir(directory+'/paused-players'):
				os.remove(directory+'/paused-players/'+i)
			continue
		player_status = player.Get('org.mpris.MediaPlayer2.Player','PlaybackStatus', dbus_interface='org.freedesktop.DBus.Properties')
		if player_status == 'Paused':
			player.Play(dbus_interface='org.mpris.MediaPlayer2.Player', reply_handler=do_nothing, error_handler=do_nothing)
			if i in os.listdir(directory+'/paused-players'):
				os.remove(directory+'/paused-players/'+i)
		
def stop():
	for i in players:
		player = bus.get_object(i, '/org/mpris/MediaPlayer2')
		player_status = player.Get('org.mpris.MediaPlayer2.Player','PlaybackStatus', dbus_interface='org.freedesktop.DBus.Properties')
		if player_status == 'Playing' or player_status == 'Stopped':
			player.Stop(dbus_interface='org.mpris.MediaPlayer2.Player', reply_handler=do_nothing, error_handler=do_nothing)
def toggle():
	playing = False
	for i in players:
		player = bus.get_object(i, '/org/mpris/MediaPlayer2')
		player_status = player.Get('org.mpris.MediaPlayer2.Player','PlaybackStatus', dbus_interface='org.freedesktop.DBus.Properties')
		if player_status == 'Playing':
			playing = True
	if playing:
		pause()
	else:
		play()
def next():
	for i in players:
		player = bus.get_object(i, '/org/mpris/MediaPlayer2')
		player_status = player.Get('org.mpris.MediaPlayer2.Player','PlaybackStatus', dbus_interface='org.freedesktop.DBus.Properties')
		if player_status == 'Playing':
			player.Next(dbus_interface='org.mpris.MediaPlayer2.Player', reply_handler=do_nothing, error_handler=do_nothing)
def previous():
	for i in players:
		player = bus.get_object(i, '/org/mpris/MediaPlayer2')
		player_status = player.Get('org.mpris.MediaPlayer2.Player','PlaybackStatus', dbus_interface='org.freedesktop.DBus.Properties')
		if player_status == 'Playing':
			player.Previous(dbus_interface='org.mpris.MediaPlayer2.Player', reply_handler=do_nothing, error_handler=do_nothing)

def getPlayerList():
	for i in bus.list_names():
		if i.startswith("org.mpris.MediaPlayer2."):
			players.append(i)

if not os.path.isdir(directory):
	os.makedirs(directory)
	if not os.path.isdir(directory+'/players'):
		os.makedirs(directory+'/players')
	if not os.path.isdir(directory+'/paused-players'):	
		os.makedirs(directory+'/paused-players')
	

if len(sys.argv)-1 is 1:
	getPlayerList()
	if sys.argv[1] == 'pause':
		pause()
	elif sys.argv[1] == 'play':
		play()
	elif sys.argv[1] == 'stop':
		stop()
	elif sys.argv[1] == 'next':
		next()
	elif sys.argv[1] == 'previous':
		previous()
	elif sys.argv[1] == 'toggle':
		toggle()
	else:
		print >> sys.stderr, "Error:  Valid commands to "+sys.argv[0]+"are: pause, play, stop, next, previous, or toggle"
else:
	print >> sys.stderr, "Usage:  "+sys.argv[0]+" [pause|play|stop|next|previous|toggle]"
