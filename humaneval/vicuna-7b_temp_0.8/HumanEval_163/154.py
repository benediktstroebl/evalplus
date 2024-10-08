
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
    for num in range(min(a, b), max(a, b) + 1):
        digit = str(num)[-1]
        if not digit in digits:
            digits.append(digit)
        else:
            if not (num + 1) % 10 == 0:
                digits.append(digit)
    return digits