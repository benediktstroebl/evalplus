
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check if n is even
    if n % 2 == 0:
        return 0

    # Convert n to digits
    digits = str(n)
    # Initialize result with 1
    result = 1

    # Iterate through digits
    for i in range(len(digits)):
        if digits[i] % 2 == 1:
            # Increment result by digits[i]
            result *= digits[i]

    return result
