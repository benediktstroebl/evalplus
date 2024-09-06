def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1) == 1
    digits(4) == 0
    digits(235) == 15
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Expected a non-negative integer input")
    
    result = False
    odd_count = 0
    
    # Iterate through each digit in the integer representation of 'n'
    for digit in str(n):
        if digit % 2 == 1:
            odd_count += 1
            result = result or digit  # Product: 1 * 3 * 5 * 7 * ...
    
    return result if odd_count else 0