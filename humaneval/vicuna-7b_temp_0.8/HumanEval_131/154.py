
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Handle the case where all digits are even
    if sum(map(lambda x: x % 2, str(n))) == 0:
        return 0
    # Handle the case where the number is a power of 2
    if n == 0 or n == 1:
        return n
    # Convert the number to a string and remove any leading zeros
    string_n = str(n)
    # Initialize the result to 1
    result = 1
    # Iterate over the digits of the string and multiply them together
    for i, digit in enumerate(string_n):
        if digit == '0':
            continue
        result *= int(digit)
    # Return the result
    return result
