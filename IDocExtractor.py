from sys import argv
import re

if len(argv) < 4:
    print("Please specify at least 3 arguments Sourcefile, Targetfile and IDoc types. {} where given".format(len(argv) - 1))
    exit(1)

pattern_string = r'(<\?xml version="1.0" encoding="UTF-8"\?><(' + r"|".join(argv[3:]) + r')>.*</\2>)'
pattern = re.compile(pattern_string)

try:
    with open(argv[1], "r") as source:
        with open(argv[2], "w") as target:
            for source_line in source:
                match = pattern.search(source_line)
                if match:
                    target.write(match.group(1) + "\n")
except FileNotFoundError:
    print("The source File you specified ({}) wasn't found".format(argv[1]))
    exit(1)
