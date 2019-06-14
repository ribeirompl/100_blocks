# 100_blocks
Focused time tracker inspired by Tim Urban's [100-Blocks article](https://waitbutwhy.com/2016/10/100-blocks-day.html)

## Project Description
There are 100 blocks representing the 100 10-minute time slots that we are awake for, in a day. 

The application (which runs entirely in the terminal) starts by asking what time you woke up this morning, so it can display the correct amount of blocks remaining for the day.

![Gui display](readme_images/startup.png?raw=true "Gui display")

The number of completed blocks total is show on the right side, while the specific wake-up and bedtime timestamps are also displayed.

![Gui display](readme_images/main_display.png?raw=true "Gui display")

You can add multiple .mp3 or .wav files into the `tunes/` folder, which will play a random tune, every 10 minutes, when a block is completed.
It will also flash a "10 min" display indicating that 10 minutes have passed.

![Settings file](readme_images/10_min.png?raw=true "Settings file")

## Future Plans
* Support for any wake-up times
* Windows support

## Dependencies
Currently, only linux operating systems are supported.
```
Python >= 3.7
Tkinter >= 8.6

ffmpeg >= 3.4.6
```

## Installation
Copy the files into a directory.

To start the application:
```sh
python3 100_blocks.py
```

