# OmniPause

OmniPause is a python program to control media players via DBus.

## Description

Have you ever wished you could control the playback of all your running media players with a single command or hotkey?
Until now, there was no real good way to do this without spending all of your free time scripting playerctl.  Now, with OmniPause, you can use a single, universal command to control all of your media players, with absolutely zero scripting required!  

## Dependencies
 * python3
 * dbus-python

## Setup
Setup is very simple.  Simply run `sudo make install` in the project directory.

## Usage
Using the program is equally simple.
 * To pause all running media players, just execute `omnipause pause`
 * To resume playback of media players paused by the program, run `omnipause play`
 * To stop all media players, run `omnipause stop`
 * To skip to the next track on all playing media players, run `omnipause next`
 * To play the previous track on all playing media players, run `omnipause previous`
 * To toggle the playback state of running media players, run `omnipause toggle`
 	* Note:  `omnipause toggle` works by pausing all of the players if any of them are playing.
	If none of them are currently playing, it resumes playback any players paused by omnipause.

## Contributing
This project was written over the course of 4-5 sleep-deprived hours.
Additionally, I am not super familiar with Python or DBus.  If you find a bug 
or find my code quality appalling, please submit a pull request.

## Licensing
This project is released under GPL 3.0.
