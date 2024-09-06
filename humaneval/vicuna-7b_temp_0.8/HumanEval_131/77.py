
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check for even case
    if sum(map(lambda x: x % 2, list(str(n)))) == 0:
        return 0
    
    # Convert to list of digits
    digits = list(map(int, str(n)))
    
    # If any digit is odd, return its product
    if any(d % 2 != 0 for d in digits):
        return d * (1 if d % 2 == 0 else 2) * digits.count(1)
    else:
        return 0
