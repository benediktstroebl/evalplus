
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
    while a <= b:
        digits = [d for d in str(a)]
        for i in range(len(digits) // 2):
            digits[i], digits[i + len(digits) // 2] = digits[i + len(digits) // 2], digits[i]
        a += 1
    return digits
