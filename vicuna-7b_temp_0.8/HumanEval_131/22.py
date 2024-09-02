
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check if all digits are even
    if sum(1 for _ in range(n)) == n:
        return 0
    
    # Initialize result
    result = 1
    
    # Iterate over digits
    for i in range(1, n):
        if i % 2 == 0:
            # Multiply by 10 and add to result
            result *= 10
            result += i
        else:
            # Multiply by 5 and add to result
            result *= 5
            result += i
    
    return result
