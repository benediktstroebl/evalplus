def double_the_difference(lst):
    """
    Sum of squares of odd integers from the list of numbers.
    
    Args:
        lst (list): List of numbers.

    Returns:
        int: Sum of squares of odd integers or 0 if the list is empty or contains only negative numbers or non-integer values.
    """
    # Check if the list is empty, or contains negative numbers or non-integer values
    # Return 0 if any of these conditions are met
    if not lst or any(n < 0 or not isinstance(n, int) for n in lst):
        return 0
    
    # Initialize result
    result = 0

    # Iterate through the list, square elements that are odd, and add to result
    for n in lst:
        if n % 2 == 1:
            result += n ** 2

    return result