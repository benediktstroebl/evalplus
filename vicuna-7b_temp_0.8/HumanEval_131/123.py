
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # check if all digits are even
    if sum(map(lambda x: x % 2, str(n))) == 0:
        return 0
    
    # check if the number is negative
    if n < 0:
        return -1
    
    # check if the number is even
    if sum(map(lambda x: x % 2, str(n))) == 0:
        return -1
    
    # get the odd digits
    odd = [int(x) for x in str(n)[1:]]
    
    # check if the number is zero
    if len(odd) == 0:
        return 0
    
    # check if the number is too big
    if len(odd) > 9:
        return -1
    
    # calculate the product of the odd digits
    product = 1
    for odd_digit in odd:
        product *= odd_digit
    
    return product
