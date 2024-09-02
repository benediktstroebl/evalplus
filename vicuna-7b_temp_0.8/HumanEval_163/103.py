
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
    while b - a > 0:
        i = a
        while i < b:
            result.append(i % 10)
            i = i // 10
        a = a + 1
    result.extend(reversed(result))
    return result
