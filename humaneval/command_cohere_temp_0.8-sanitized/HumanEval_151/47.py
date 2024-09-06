def double_the_difference(lst):
    """
    Sum of squares of odd integers from the list ignoring negatives and non-integers.
    
    Returns 0 if the list is empty or non-numeric.
    """
    if not lst:
        return 0
    
    odd_squares = sum(x**2 for x in lst if x % 2 and isinstance(x, int) and x >= 0)
    return odd_squares