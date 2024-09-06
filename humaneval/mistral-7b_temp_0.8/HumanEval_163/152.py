
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    digits = []
    while a <= b:
        a *= 10
        while a >= 10:
            digit = a // 10
            if digit % 2 == 0:
                digits.append(digit)
            a %= 10
    return digits

