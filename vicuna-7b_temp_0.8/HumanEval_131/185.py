
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Handle the base case
    if n < 2:
        return 0
    
    # Find the first digit that is odd
    d = n // 2
    
    # If the first digit is odd, the product is n/2
    if d % 2 == 1:
        return n // d
    
    # If the first digit is even, find the highest odd digit
    while d % 2 == 0:
        d /= 2
    
    # If there is no highest odd digit, return 0
    if not d:
        return 0
    
    # The product is d*d*...*2*1
    return d * (d // 2) * (d // 4) * ... * (d // 2 * d % 2) * (d // 2 + 1)