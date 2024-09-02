
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # The algorithm is simple. We keep track of the smallest unused integer in
    # the range [a, b), and whenever we find an integer with an odd digit, we
    # subtract 1 from that integer.
    #
    # The smallest unused integer in the range [a, b) is the sum of the
    # integers from 0 to b-1, minus the sum of the integers from 0 to a-1.
    #
    # To find the smallest unused integer in the range [a, b), we can simply
    # check all the integers between a and b, and keep the one that is not
    # used yet.

    # The loop will run from a to b. The variable k is the index of the
    # current integer in the range [a, b), and d is the digit of the current
    # integer.
    k = a
    d = a % 10
    b = b - a
    result = []
    for j in range(b):
        result.append(d)
        d = int(a / 10)
        a = int(a % 10)
    return result
