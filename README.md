# OmniPause

OmniPause is a python program to control media players via DBus.

## Description
### Correction
I was made aware of the project playerctl recently.  It appears to do all of the same things as this project.  However, I now have no idea what to put in the description section, so I will just leave the existing description prefaced with this correction.  

Have you ever wished you could control the playback of all your running media players with a single command or hotkey?
Until now, there was no real good way to do this.  If you wanted a universal pause/play hotkey, you were pretty much out of luck.  Now, with OmniPause, you can use a single, universal command to control all of your media players.  

## Dependencies
 * python2
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
