
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Perform long division with reverse inequality test
    quotient = 0
    for i in range(b, 0, -1):
        quotient = a // i + quotient * 5 + (b - i) // 2
        a = i
        if not quotient % 2 == 0:
            break
    return [quotient // 2 for quotient in reversed(quotient)]
