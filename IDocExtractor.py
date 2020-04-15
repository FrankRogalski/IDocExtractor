import argparse
import re

parser = argparse.ArgumentParser(description='Create a file of changed Customers from three unfiltered xls files')

parser.add_argument("-s","--source", dest="source_path", help="The Datahub log from which this programm will retrieve the IDocs", required=True)
parser.add_argument("-t", "--target", dest="target_path", help="The file which will contain the IDocs", required=True)
parser.add_argument("-it", "--idoc-types", dest="idoc_types", nargs="+", help="The IDoc types that will be filtered", required=True)

args = parser.parse_args()

def main():
    pattern_string = r'(<\?xml version="1.0" encoding="UTF-8"\?><(' + r"|".join(args.idoc_types) + r')>.*</\2>)'
    pattern = re.compile(pattern_string)

    try:
        with open(args.source_path, "r") as source:
            with open(args.target_path, "w") as target:
                for source_line in source:
                    match = pattern.search(source_line)
                    if match:
                        target.write(match.group(1) + "\n")
    except FileNotFoundError:
        print(f"The source File you specified ({args.source_path}) wasn't found")
        exit(1)

if __name__ == "__main__":
    main()