
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Handle the case when all digits are even.
    if n % 2 == 0:
        return 0
    
    # Keep track of the odd digits and the product.
    odd_digits = [int(d) for d in str(n)]
    product = 1
    
    for d in odd_digits:
        # Multiply the product by d.
        product *= d
    
    # Return the product.
    return product
