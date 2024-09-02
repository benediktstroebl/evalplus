
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    integers = []

    if a > b:
        i = b
        while i <= a:
            if i % 2 == 0:
                integers.append(i)
            i += 1
    else:
        i = a
        while i <= b:
            if i % 2 == 0:
                integers.append(i)
            i += 1

    return integers
