
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # n is the number of digits between a and b
    n = abs(b - a)

    # digits is a list of n digits, from the left to the right
    digits = [str(i) for i in range(a, b+1)]
    digits.reverse()
    result = []

    # generate the even digits
    for i in range(1, n+1):
        result.append(digits[i//2])

    return result
