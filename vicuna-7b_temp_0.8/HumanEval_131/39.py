
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Handle base case
    if n < 10:
        return n
    
    # Check if all digits are even
    if sum(int(d) for d in str(n)) % 2 == 0:
        return 0
    
    # Compute the odd digits product
    odd_digits = [int(d) for d in str(n)]
    odd_digits.sort()
    product = 1
    for digit in odd_digits:
        product *= digit
    return product
