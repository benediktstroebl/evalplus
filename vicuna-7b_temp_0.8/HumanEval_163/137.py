
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
    for num in range(a, b+1):
        digit = num % 10
        if digit > 0:
            digits.append(digit)
            num //= 10
    if num > 0:
        digits.append(num % 10)
    return digits
