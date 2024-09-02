
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Write your code here.
    lst = list(range(a, b + 1))
    for i in lst:
        if (i % 2) != 0:
            lst.remove(i)
    return lst
