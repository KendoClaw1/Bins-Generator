# Bins-Generator

this tool will generate a list of CC's based on a bin provided by the user, then starts verifying the generated CC's using donate.mozilla.com payment gateway. (Mozilla uses Luhn Algorithm as a first check) 


usage: generator.py [-h] [-b BIN] [-n N] [-o result.txt]

Bins Generator by KendoClaw1

optional arguments:

  -h, --help     show this help message and exit

  -b BIN         The bin to generate CC's

  -n N           Number of Bins to generate (Default = 50)

  -o result.txt  Output file

## Usage example:

python generator.py -b 471786xxxxxxxxxx -n 100 -o result.txt
