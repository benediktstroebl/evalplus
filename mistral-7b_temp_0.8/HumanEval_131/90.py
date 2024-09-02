
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # base case
    # if n is less than zero, then return 0
    if n < 0:
        return 0
    # if n is 0, then return 0
    elif n == 0:
        return 0
    # create a new variable that will store the product of the odd digits
    product = 1
    # create a new variable that will store the current digit
    current_digit = n % 10
    # create a new variable that will store the remainder of the quotient of dividing n by 10
    remainder = n // 10
    # if the current digit is odd, then multiply the product by the current digit
    if current_digit % 2 != 0:
        product *= current_digit
    # if the remainder is not 0, then recursively call the function with the remainder as the argument
    if remainder != 0:
        product *= digits(remainder)
    # return the product of the odd digits
    return product
