
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Remove any leading zeros
    a = str(a)
    b = str(b)
    digits = []
    while a < b:
        # Get the digits in the current number
        current_digits = map(str, range(int(a) - int(b)))
        # Add the digits in the correct order
        digits.extend(current_digits[::-1])
        # Update the number
        a = b
        b = int(b)
    return digits
