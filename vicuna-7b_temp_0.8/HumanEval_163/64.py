
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
    while a <= b:
        d = a
        while d % 2 == 0:
            result.append(d)
            d = d // 2
        a = b
        b = b + 2
    return result
