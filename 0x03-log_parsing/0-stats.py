#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics:

    Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size>
    Each 10 lines and after a keyboard interruption
    (CTRL + C), prints those statistics since the beginning: """
import sys


size = 0
# Initialized an empty dict to store the count of status codes
status_codes = {}
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
# var number of lines processed
count = 0


def print_status_code():
    """prints statistics since the beginning of Each 10 lines
    """
    print("File size:", size)
    for key in sorted(status_codes):
        print(key + ":", status_codes[key])

if __name__ == "__main__":
    try:
        for line in sys.stdin:
            if count == 10:
                print_status_code()
                count = 1
            else:
                count += 1

            elements = line.split()
            try:
                size += int(elements[-1])
            except (IndexError, ValueError):
                pass
            try:
                # Get second-to-last element as the <status_code>
                status_code = elements[-2]
                if status_code in valid_codes:
                    if status_code not in status_codes:
                        # If <status_code> is not in status_codes dict,
                        # add it as a new key, count=1
                        status_codes[status_code] = 1
                    else:
                        # If <status_code> is already in status_codes dict,
                        # increment its count
                        status_codes[status_code] += 1
            except IndexError:
                # Ignore IndexError if the element doesn't exist
                pass
        print_status_code()

    except KeyboardInterrupt:
        print_status_code()
        raise
