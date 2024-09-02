
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Get a and b in non-negative integers
    a = abs(a)
    b = abs(b)
    # Loop through numbers from a to b
    for i in range(a, b + 1):
        # Initialize an empty list to store even digits
        digits = []
        # Loop through digits from 0 to i
        for j in range(2, 10):
            # If the current digit is even, append it to the list
            if j in str(i):
                digits.append(j)
        # If the list is not empty, append it to the result
        if digits:
            result.extend(digits)
    return result
