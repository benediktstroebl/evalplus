
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Handle the base case: all digits are even
    if all(c in '04689' for c in str(n)):
        return 0
    
    # Handle the other cases: odd digit(s) exist
    if n % 2 != 0:
        # Get the odd digit(s)
        odd_digits = [int(d) for d in str(n)[1:]]
        
        # Compute the product
        product = 1
        for digit in odd_digits:
            product *= digit
        return product
