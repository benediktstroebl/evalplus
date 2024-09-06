
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if b <= a:
        return []

    digits = []
    while a >= 10:
        digits.append(a % 10)
        a = a // 10
    digits.append(a % 10)

    for _ in range(b - a - 1):
        digits.append(digits[-1])

    return digits
