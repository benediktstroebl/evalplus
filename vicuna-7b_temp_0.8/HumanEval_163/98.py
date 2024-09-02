
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
    if a == b:
        return [a]
    digits = []
    for i in range(a, b + 1):
        digit = int(str(i)[-1])
        if i > a and i % 2 == 0:
            digits.append(digit)
    return digits
