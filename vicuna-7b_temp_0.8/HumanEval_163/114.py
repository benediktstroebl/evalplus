
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Create a list to store the even digits
    digits = []

    # Loop through the range a to b, excluding a and b
    for num in range(a+1, b+1):
        # Append the digit num to the list of even digits
        digits.append(num % 2)

    return digits
