
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # start = max(a, b)
    # end = min(a, b)
    #
    # if end % 2 == 1:
    #     end -= 1
    #
    # for i in range(start, end, -2):
    #     yield i

    if a > b:
        a, b = b, a

    for i in range(a, b+1, 2):
        yield i

