
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    result = 1
    #loop over the digits
    for digit in str(n):
        #check if the digit is odd
        if int(digit) % 2 == 1:
            #if so, add to product
            result *= int(digit)
    return result

