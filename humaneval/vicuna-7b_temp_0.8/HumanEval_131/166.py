
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Handle the base case where n is 0
    if n == 0:
        return 0
    
    # Handle the case where n is 1
    if n == 1:
        return n
    
    # Keep track of the sum of the digits
    sum = 0
    for i in range(len(str(n))):
        sum += int(str(n)[i])
    
    # Check if all digits are even
    if all(c == 0 for c in sum):
        return 0
    
    # Handle the case where n is odd
    n = n % 2
    return sum // 2
