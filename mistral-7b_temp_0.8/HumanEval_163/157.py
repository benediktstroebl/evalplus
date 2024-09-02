
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
    while a <= b:
        integer = a
        while integer > 0:
            last_digit = integer % 10
            if last_digit % 2 == 0:
                integers.append(last_digit)
                break
            integer = integer // 10
        a += 1
    return integers
