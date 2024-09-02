
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Check if a is less than b
    if a < b:
        # Reverse the input range
        b, a = a, b
    # Initialize the list to store the even digits
    digits = [i for i in range(a, b + 1) if i % 2 == 0]
    # Reverse the list again to get the ascending order
    digits = digits[::-1]
    return digits