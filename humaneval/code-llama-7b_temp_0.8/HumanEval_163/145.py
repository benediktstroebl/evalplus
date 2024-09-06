
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a < b:
        a, b = b, a
    digits = []
    if a % 2 == 0:
        digits.append(str(a))
    a += 2
    while a < b:
        if a % 2 == 0:
            digits.append(str(a))
        a += 2
    return digits

