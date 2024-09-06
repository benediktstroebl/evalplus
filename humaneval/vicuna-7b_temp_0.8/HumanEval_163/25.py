
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Define a helper function to calculate the digits of a number
    def digits(n):
        # Check if n is negative or zero
        if n < 0 or n == 0:
            return -1

        # Initialize a list to store the digits
        digits = []

        # For each digit in n, append it to the list
        for i in range(10):
            digits.append(n // i)
            n = n // 10

        return digits

    # Check if a and b are positive integers
    if a <= 0 or b <= 0:
        return []

    # Calculate the digits of a and b
    digits_a = digits(a)
    digits_b = digits(b)

    # Initialize a list to store the even digits between a and b
    digits = []

    # For each digit from digits_a to digits_b (inclusive), append it to the list
    for i in range(1, len(digits_a)):
        digits.append(digits_a[i])

    # Add the digit that is not in the list (i.e., the next digit in the sequence)
    digits.append(digits_a[len(digits_a)])

    # For each digit from digits_b to digits_a (inclusive), append it to the list
    for i in reversed(range(1, len(digits_b))):
        digits.append(digits_b[i])

    # Return the list of even digits
    return digits
