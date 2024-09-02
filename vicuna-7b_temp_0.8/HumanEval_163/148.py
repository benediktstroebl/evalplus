
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # If a is less than b, there are no even digits.
    if a < b:
        return []

    # If b is even, the only even digit is 0.
    if b % 2 == 0:
        return [0, 1] + generate_integers(b-1, a)

    # If a is even or a is greater than b, there are no even digits.
    # Even or greater values can only have odd digits, which are 1, 3, 5, 7, 9.
    # Thus, we can't find any even digits.
    else:
        return []
