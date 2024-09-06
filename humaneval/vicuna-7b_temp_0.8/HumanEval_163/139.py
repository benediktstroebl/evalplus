
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
    while a < b:
        middle = (a + b) // 2
        result.append(middle % 10)
        a = b
        b = middle + 1
    result.append(b % 10)
    return result
