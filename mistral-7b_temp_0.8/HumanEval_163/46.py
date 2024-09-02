
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    even_digits = []

    if a < b:
        while a <= b:
            if a % 2 == 0:
                even_digits.append(a)
            a += 1
    else:
        while b <= a:
            if b % 2 == 0:
                even_digits.append(b)
            b += 1

    return even_digits
