
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    # check whether input is valid
    if a == b or not isinstance(a, int) or not isinstance(b, int) or a < 0 or b < 0:
        return []

    # for faster processing
    if a > b:
        a, b = b, a

    return [num for num in range(a, b + 1) if num % 2 == 0]
