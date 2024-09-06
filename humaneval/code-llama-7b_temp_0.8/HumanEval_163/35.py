
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # an even integer is one that ends with 0, 2, 4, 6, or 8.
    # for example: 24, 26, 28, 30, etc.
    # if a is less than b, then the odd integer between a and b is a + 1,
    # and we check that integer to see if it is between a and b.

    # if a is greater than b, then the odd integer between a and b is b - 1,
    # and we check that integer to see if it is between a and b.

    # if a is even and b is even, then the even digits between a and b are
    # the even integers between a and b.
    # if a is even and b is odd, then the even digits between a and b are
    # the even integers between a and the lowest even integer between a and b.
    # if a is odd and b is even, then the even digits between a and b are
    # the even integers between the highest even integer between a and b and b.
    # if a is odd and b is odd, then the even digits between a and b are
    # the even integers between the highest even integer between a and b and
    # the lowest even integer between a and b.

    #In the first two cases, if there are no even integers between a and b,
    #then an empty list is returned.

    #In the last two cases, the generated list of even integers is either empty
    #or contains an odd integer. In the latter case, the list is reduced to
    #remove the odd integer.

    if a > b:
        a, b = b, a

    if a % 2 != 0:
        a += 1

    if b % 2 == 0:
        if a > b:
            return []
        return [x for x in range(a, b + 1, 2)]
    else:
        if b - a == 1:
            return []
        else:
            return [x for x in range(a, int(b + 1 / 2), 2)]

