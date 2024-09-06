
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        raise Exception("a must be less than or equal to b")
    if a % 2 != 0 or b % 2 != 0:
        raise Exception("a and b must be even")

    result = []
    while a <= b:
        if a % 2 == 0:
            result.append(a)
        a += 1

    return result

