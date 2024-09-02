
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # The range of integers between a and b is [a, b]
    # We want to generate the even digits in the range [a, b], so we can
    # use the modulus operator to get the remainder when an integer is
    # divided by 2.
    # We can then take the first n digits of the sequence of remainders
    # to get the even digits between a and b.
    #
    # However, since we want to generate the even digits in ascending order,
    # we need to reverse the list.
    return [2 * digit for digit in reversed(range(a, b + 1)) if digit % 2 == 0]
