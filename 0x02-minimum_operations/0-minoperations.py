#!/usr/bin/python3
"""
Main file for testing
"""


def minOperations(n: int) -> int:
    """Returns the minimum operations required to archieve n characters."""

    result = 0
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                result += i
                n = n // i
                break
    return result


if __name__ == '__main__':

    n = 1
    print("Min # of operations to reach {} char: {}".format(
        n, minOperations(n)))
    n = 3
    print("Min # of operations to reach {} char: {}".format(
        n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(
        n, minOperations(n)))
    n = 12
    print("Min # of operations to reach {} char: {}".format(
        n, minOperations(n)))
    n = 12
    print("Min # of operations to reach {} char: {}".format(
        n, minOperations(n)))
