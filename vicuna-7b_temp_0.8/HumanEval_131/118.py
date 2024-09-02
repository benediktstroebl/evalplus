
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check if all digits are even, in which case return 0
    if sum(int(d) for d in str(n)) % 2 == 0:
        return 0
    
    # Otherwise, return the product of the odd digits
    return int(n) % 1000000007 * (1000000009 * (1000000007 + 1)) % 1000000009
