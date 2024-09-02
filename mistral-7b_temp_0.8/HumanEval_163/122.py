
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # your code goes here

    # first determine which of a and b is larger
    if a > b:
        a, b = b, a

    # If there are no even integers, return an empty list
    if a % 2 != 0:
        return []

    # If there are no even integers, return an empty list
    if b % 2 != 0:
        return []

    # If there are only one even integers, return a list with that number
    if a == b:
        return [a]

    # If there are two even integers, return a list with those numbers
    if a + 2 == b:
        return [a, b]

    # If there are more than two even integers, return a list with all the
    # even integers between a and b
    else:
        return [a + i * 2 for i in range(0, (b - a) // 2 + 1)]
