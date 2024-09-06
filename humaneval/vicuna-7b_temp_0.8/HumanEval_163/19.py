
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    result = set()
    while a <= b:
        num = (a + b) // 2
        result.add(num % 2)
        a = b
        b = num + 1
    return sorted(result)
