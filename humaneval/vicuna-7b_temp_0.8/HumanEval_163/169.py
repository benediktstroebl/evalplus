
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Check that a is not greater than b
    if a > b:
        return []

    # Create a list to store the even digits
    digits = []

    # Loop from left to right
    for i in range(a, b+1):
        # Loop from right to left
        for j in reversed(range(b, i-1)):
            # If the number is even, add its digits to the list
            if j+1 == b:
                digits.append(i)
            else:
                digits.append(i-j-1)
        digits.append(i)

    return digits
