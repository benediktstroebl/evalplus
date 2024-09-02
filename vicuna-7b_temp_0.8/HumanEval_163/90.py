
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    i = 0
    result = []
    while a <= b:
        while b % 2 == 0:
            result.append(b // 2)
            b = b // 2
        a = a + 1
        i += 1
    return result
