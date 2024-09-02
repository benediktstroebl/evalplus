
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
        digits = [int(d) for d in str(a)]
        if sum(digits) % 2 == 0:
            result.append(sum(digits))
            a = a + 1
        else:
            a = a + 1
    return result
