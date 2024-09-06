
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Base case: If n is 0, return 0.
    if n == 0:
        return 0
    
    # If the number is odd, return its digits product.
    if n % 2 == 1:
        return n * digits(n // 2)
    
    # If the number is even, return 0.
    return 0
