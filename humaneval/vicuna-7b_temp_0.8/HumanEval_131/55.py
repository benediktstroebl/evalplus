
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Remove leading zeros
    n = abs(n)
    if n == 0:
        return 0
    # Check if all digits are even
    if sum(map(lambda x: x % 2, str(n))) == 0:
        return 0
    # Split the string into an array of digits
    digits = [int(d) for d in str(n)]
    # Initialize result to 0
    result = 0
    # Iterate through the digits array
    for i, d in enumerate(digits):
        # If the current digit is odd, multiply the result by d
        result = result * d * (i + 1)
    return result
