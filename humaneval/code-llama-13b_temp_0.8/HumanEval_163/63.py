
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    # The ord() function converts a single character to the corresponding ASCII integer value.
    # When we call it on a string, it returns an array containing the integers for each character in the string.
    # This isn't really necessary, but I find it more readable than using the range() function.
    return sorted([n for n in map(ord, str(a)) if n % 2 == 0 and n in range(ord(str(b)[0]), ord(str(b)[1]) + 1)])
