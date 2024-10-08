
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    result = []
    for num in range(min(a, b), max(a, b) + 1):
        digits = ""
        while num > 0:
            digits = digits * 10 + (num % 10)
            num = num / 10
        result.append(digits)
    return result
