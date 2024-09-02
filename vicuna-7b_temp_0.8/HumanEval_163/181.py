
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Create a new list to store the even digits
    digits = []

    # Iterate through the range of integers from a to b
    for i in range(a, b + 1):
        # Check if the current integer is even
        if i % 2 == 0:
            # If the current integer is even, append it to the list
            digits.append(i)

    # Return the list of even digits
    return digits
