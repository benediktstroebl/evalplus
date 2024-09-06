
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    n = max(a, b)
    digits = []
    while n > 0:
        d = n % 10
        digits.append(d)
        n = n // 10
    digits.reverse()
    return digits
