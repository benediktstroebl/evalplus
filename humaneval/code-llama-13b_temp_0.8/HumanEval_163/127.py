
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
    for num in range(a, b + 1):
        digits.append(num)
    even_digits = []
    for num in digits:
        if num % 2 == 0:
            even_digits.append(num)
    even_digits.sort()
    return even_digits
