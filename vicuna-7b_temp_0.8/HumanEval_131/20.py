
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check if the input is even
    if not n % 2:
        return 0

    # Loop through the digits and add them up
    digits = [int(d) for d in str(n)]
    result = 0
    for digit in digits:
        if digit % 2 != 0:
            result += digit
    return result
