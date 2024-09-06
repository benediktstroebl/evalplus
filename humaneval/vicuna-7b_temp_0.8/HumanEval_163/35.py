
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

    # Loop through the range of numbers from a to b
    for i in range(a, b+1):
        # Get the digits of the number
        digits_str = str(i)
        digits_num = int(digits_str)

        # Check if the number is even
        if digits_num % 2 == 0:
            # Add the current digit to the list
            digits.append(digits_num % 10)

    return digits
