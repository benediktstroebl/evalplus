def double_the_difference(lst):
    """
    Sum of squares of odd integers from the list, while ignoring negatives and non-integers.
    
    Returns 0 if the input list is empty.
    
    """
    result = 0
    # Use a flag to track if any valid odd integer is encountered.
    has_valid_odd = False
    
    # Iterate through the list and identify integers and oddities.
    for num in lst:
        if isinstance(num, int) and num % 2 != 0:
            has_valid_odd = True
            result += num ** 2
            
    # If no valid odd integer is found, return 0.
    if not has_valid_odd:
        return 0
    
    return result