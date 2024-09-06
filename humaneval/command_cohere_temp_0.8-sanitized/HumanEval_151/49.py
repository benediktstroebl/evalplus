def double_the_difference(lst):
    """
    Sum of squares of odd integers from the list ignoring negatives and non-integers.
    
    Returns 0 if the list is empty or only contains negatives, non-integers, or zeros.
    """
    if not lst or all(x <= 0 or not isinstance(x, int) or x % 2 == 0 for x in lst):
        return 0
    
    return sum(x**2 for x in lst if x % 2 != 0)