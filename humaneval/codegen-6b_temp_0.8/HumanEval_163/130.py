
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # if a is even and b is even, then they are the same number
    if a % 2 == 0 and b % 2 == 0:
        return [a, b]

    # if a is smaller than b, flip them
    if a < b:
        a, b = b, a

    # if a is odd and b is odd, then they are the same number
    if a % 2 != 0 and b % 2 != 0:
        return [a, b]

    # if a and b are both odd, then they are the same number
    if a % 2 != 0 and b % 2 != 0:
        return [a, b]

    # integer_list = ["%d" % x for x in range(a, b + 1) if x % 2 == 0]
    integer_list = []
    for x in xrange(a,b+1):
        if x % 2 == 0:
            integer_list.append(x)

    return integer_list
