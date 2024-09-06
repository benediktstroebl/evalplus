
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Find the first number in the range of a and b that is not a power of 2
    mid = max(a, b) // 2 + 1
    # If the first number is not a power of 2, the rest of the digits will be
    # the even digits of the first number
    if mid not in (2**n * n for n in range(0, mid)):
        # All the digits are even
        return [2 * i for i in range(a, b + 1)]
    else:
        # Find the digit of the first number that is not 0
        digit = mid % 10
        # Find the index of the digit in the range of a and b
        idx = mid - digit
        # Generate the even digits of the first number
        digits = [2 * i for i in range(a, b + 1)]
        # Filter out all the digits but the digit at the specified index
        digits = [d for d in digits if d // 10**idx == d]
        return digits
