# Python-validar-mysql
Python GUI program that checks the system's OS, RAM, and disk usage, and optimizes MySQL's my.ini file with the recommended values. Displays results and optimization status using a Tkinter GUI.


# Check System
This Python script checks the system to ensure that it meets certain requirements. It uses the tkinter module to create a simple GUI that allows the user to check the system and optimize the my.ini file for MySQL.

# Requirements
Python 3.x
psutil
tkinter

# Installation
Clone the repository or download the source code.
Install the psutil module by running pip install psutil in your terminal or command prompt.
Run the check_system.py script.

# Usage
Launch the check_system.py script.
Click the "VALIDAR" button to check the system.
If the system passes the check, the results will be displayed in green text.
If the system fails the check, the results will be displayed in red text.
Click the "OTIMIZAR my.ini" button to optimize the my.ini file for MySQL.
A success message will be displayed if the optimization is successful.

# Notes
The script checks for a 64-bit operating system, a Windows version greater than 7, and at least 4 GB of RAM and 60 GB of disk space.
The innodb_buffer_pool_size parameter in the my.ini file is optimized based on the amount of RAM available.
The max_connections parameter in the my.ini file is set to 900 or 1200, depending on whether the server-id parameter is set.
This script is only compatible with Windows operating systems.
This script should be run with administrator privileges to modify the my.ini file.

# Credits
This script was created by Enzo Xavier as a project for VSM INFORMATICA. It uses the following modules:

tkinter (built-in)
psutil (https://github.com/giampaolo/psutil)
