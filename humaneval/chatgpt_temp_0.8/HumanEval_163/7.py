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
    for num in range(a, b+1):
        digits = [int(digit) for digit in str(num)]
        for digit in digits:
            if digit % 2 == 0 and digit not in even_digits:
                even_digits.append(digit)
    return sorted(even_digits)
