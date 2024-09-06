
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check if all digits are even, return 0 if so
    if sum(int(d) for d in str(n)) % 2 == 0:
        return 0
    # Use a list to store the digits and multiply them
    digits = [int(d) for d in str(n)]
    product = digits[0]
    for digit in digits[1:]:
        product *= digit
    return product
