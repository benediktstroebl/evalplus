
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # check if all digits are even
    if sum(1 for d in n if d % 2 == 0) == n:
        return 0
    
    # compute the sum of the digits
    digits = sum(map(int, str(n)))
    
    # check if any digit is odd
    if digits % 2 != 0:
        return digits
    
    # loop through the digits and compute the product
    for i in range(1, len(digits)):
        product = digits * (digits[0] - i)
        
        # update the digits
        digits = product + (digits[i+1] - digits)
        
        # check if the updated digits are odd
        if digits % 2 != 0:
            return digits
    
    return 0
