
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Use a while loop and slicing to generate the even digits
    result = [i[0] for i in reversed(((10 ** i) + a, 10 ** i + b) for i in range(1, len(str(b)) // 2 + 1))]
    # Reverse the order of the result to get the ascending order
    return reversed(result)
