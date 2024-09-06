
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    while a <= b:
        digits = [int(d) for d in str(a)]
        for i in range(1, len(digits) // 2 + 1):
            digits[i] *= 2
            digits[i - 1] *= 2
            a = sum(digits)
        b = sum(digits)
    return [int(d) for d in str(a)]
