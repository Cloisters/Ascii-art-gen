# Ascii-art-gen
ASCII Art Generator
This is a Python program that generates ASCII art from text using the Pyfiglet library.

Requirements
Python 3.x
Pyfiglet library (install with pip install pyfiglet)
Usage
To generate ASCII art, run the ascii_art.py script with the desired text and font options. The output will be printed to the console by default.

arduino
Copy code
python ascii_art.py -t "Hello, world!" -f standard
Options
-t, --text TEXT: Specify the text to convert to ASCII art (default is "Hello, world!")
-f, --font FONT: Specify the font to use for the ASCII art (default is "standard")
-o, --output OUTPUT: Specify the output file for the ASCII art
-h, --help: Display help text
Fonts
To see a list of available fonts, run the ascii_art.py script with the --list-fonts option:

css
Copy code
python ascii_art.py --list-fonts
