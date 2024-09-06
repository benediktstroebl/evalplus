
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    # get list of integers between a and b
    nums = [i for i in range(a, b + 1)]

    # get set of even integers between a and b
    evens = [i for i in nums if i % 2 == 0]

    # sort the list of even integers
    evens.sort()

    return evens

