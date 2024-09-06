
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
    for x in range(a, b + 1):
        digit = x
        while digit:
            digit, last = divmod(digit, 10)
            if last % 2 == 0:
                result.append(last)
    return result

