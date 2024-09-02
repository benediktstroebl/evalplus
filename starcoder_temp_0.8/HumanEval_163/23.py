
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    list_integers = []
    if a > b:
        return list_integers
    else:
        for integer in range(a, b+1):
            if integer % 2 == 0:
                list_integers.append(integer)
    return list_integers

