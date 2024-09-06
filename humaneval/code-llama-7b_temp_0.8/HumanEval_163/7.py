
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    #   Set up our list of digits
    if a > b:
        digits = [2, 4, 6, 8]
    elif a == b:
        digits = []
    else:
        digits = [i for i in range(a, b + 1)]
        digits = [i for i in digits if i % 2 == 0]
    return digits
