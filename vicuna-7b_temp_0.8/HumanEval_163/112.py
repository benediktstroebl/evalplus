
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
        return []
    digits = [int(d) for d in str(a)]
    for i in range(1, b - a + 1):
        digits[i] = 0
    result = [int(d) for d in str(a)]
    for i in range(1, b - a + 1):
        result[i] = result[i] + 2 * result[i - 1]
    return result
