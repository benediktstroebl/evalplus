
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Use a range of a and b to generate all possible digits between them
    digits = list(range(a, min(b+1, 10**len(str(b)))+1))

    # Remove all odd digits from the list of digits
    digits = [digit for digit in digits if digit % 2 == 0]

    # Sort the remaining digits in ascending order
    digits.sort()

    # Return the sorted list of even digits
    return digits
