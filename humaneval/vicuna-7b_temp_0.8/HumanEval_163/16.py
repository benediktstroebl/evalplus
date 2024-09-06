
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Combine a and b to get the range
    range_start, range_end = max(a, b), min(a, b)
    # Filter out the odd digits
    digits = [digit for digit in str(range_end) if digit not in str(range_start)]
    # Convert the digits to integers
    return [int(digit) for digit in digits]
