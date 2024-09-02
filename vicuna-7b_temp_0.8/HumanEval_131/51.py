
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check if all digits are even
    if sum(map(lambda x: x % 2, n)) == 0:
        return 0
    
    # Check if n is odd
    if n % 2 == 0:
        return 0
    
    # Return the product of the odd digits
    digits = [n // x if x % 2 == 1 else 0 for x in range(1, int(n / 2) + 1)]
    return sum(digits)
