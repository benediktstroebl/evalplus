
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Define a helper function to check if a digit is odd
    def odd_digit(x):
        return x % 2 == 1
    
    # Iterate through the digits and multiply them together
    # Return 0 if all digits are even
    product = 0
    for i in range(10):
        if odd_digit(int(n) / 10 ** i):
            product *= int(n) / 10 ** i
        else:
            product += int(n) / 10 ** i
    return product
