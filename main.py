import pyfiglet
import sys


def display_help():
    print("Usage: python ascii_art.py [options]")
    print("Options:")
    print("  -t, --text TEXT\t\tSpecify the text to convert to ASCII art")
    print("  -f, --font FONT\t\tSpecify the font to use for the ASCII art")
    print("  -o, --output OUTPUT\t\tSpecify the output file for the ASCII art")
    print("  -h, --help\t\t\tDisplay this help message")
    print("  --list-fonts\t\t\tDisplay a list of available fonts")
    sys.exit()

# Check for the --list-fonts option
if "--list-fonts" in sys.argv:
    fonts = pyfiglet.FigletFont.getFonts()
    print("Available fonts:")
    for font in fonts:
        print(font)
    sys.exit()

# Set default values for options

display_help()

i = 1
while i < len(sys.argv):
    arg = sys.argv[i]
    if arg in ["-t", "--text"]:
        i += 1
        text = sys.argv[i]
    elif arg in ["-f", "--font"]:
        i += 1
        font = sys.argv[i]
    elif arg in ["-o", "--output"]:
        i += 1
        output_file = sys.argv[i]
    elif arg in ["-h", "--help"]:
        display_help()
    else:
        print("Error: invalid argument {}".format(arg))
        display_help()
    i += 1


ascii_art = pyfiglet.figlet_format(text, font=font)
if output_file:
    with open(output_file, "w") as f:
        f.write(ascii_art)
else:
    print(ascii_art)
