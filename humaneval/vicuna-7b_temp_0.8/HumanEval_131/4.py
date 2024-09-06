
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # binary representation of n
    b, n = n//2, n//2
    
    # initialize result with 1
    r = 1
    
    # loop over digits
    for i in range(1, n+1):
        # convert digit to binary
        digit = int(str(i)[2:])
        
        # set bit 1 in result
        r = r*10 + digit + (b*2**(n-i-1))&1
        
        # toggle bit 1 in b
        b = b^2
    
    return r

n = int(input("Enter a positive integer: "))
result = digits(n)
print("The result is", result)