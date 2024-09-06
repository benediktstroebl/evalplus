
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Perform multiplication and slicing to get the desired digits
    digits = [int(i) for i in str(a) + str(b) if i.isdigit()]
    result = [0] * len(digits)
    for i in range(0, len(digits), 2):
        result[i:i+2] = digits[i] + digits[i+1]
    return result
