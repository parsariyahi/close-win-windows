# close-win-windows
Script to close specified windows

| WARNING: when you close the process, it will close the process in all desktops in anywhere. |
| --- | 

## Usage
1. first put your desier and most used apps that you want to close.
2. then run the script, the script will close all the process that are in `proc_names.txt`,
    > the script uses `taskkill /im` to kill the process, and will not use `/f` to force.

