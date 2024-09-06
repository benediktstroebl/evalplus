
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
    if a >= b:
        return result
    if a % 2 == 0:
        result.append(a)
    if b % 2 == 0:
        result.append(b)

    while a < b:
        if (a % 2 == 0) and (b % 2 == 0):
            if a < b:
                result.append(a)
            else:
                result.append(b)
        a += 1
        b += 1

    return result
