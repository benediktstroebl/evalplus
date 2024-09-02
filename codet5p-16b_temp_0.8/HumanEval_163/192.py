
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    result = []

    if (a % 2!= 0):
        a = a - 1
    if (b % 2!= 0):
        b = b + 1

    if a < b:
        for i in range(a, b - 1, -1):
            if i % 2 == 0:
                result.append(i)

    else:
        for i in range(a, b + 1):
            if i % 2 == 0:
                result.append(i)

    return result

