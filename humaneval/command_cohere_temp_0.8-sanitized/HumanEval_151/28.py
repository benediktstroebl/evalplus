def double_the_difference(lst):
    """
    Sum of squares of odd numbers in a list of integers, with negative numbers ignored.
    
    Args:
        lst (list): List of numbers.
    
    Returns:
        int: Sum of squares of odd numbers, or 0 if the list is empty or contains only even or negative numbers.
    """
    # Ensure the list contains only integers and is non-empty
    valid_numbers = [x for x in lst if x >= 0 and isinstance(x, int)]
    if not valid_numbers:
        return 0
    
    odd_numbers = [x for x in valid_numbers if x % 2 == 1]
    squared_odd = [x ** 2 for x in odd_numbers]
    
    return sum(squared_odd)