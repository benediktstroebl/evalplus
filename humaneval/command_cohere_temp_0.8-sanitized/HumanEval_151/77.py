def double_the_difference(lst):
    """
    Sum of squares of odd numbers in a list, while ignoring negative or non-integer numbers.

    Args:
        lst (list): List of numbers.

    Returns:
        int: Sum of squares of odd numbers, or 0 if the list is empty or contains only even or negative numbers.
    """
    result = 0
    # Initialize a flag to track if any valid odd number is found.
    found_valid_odd = False
    
    # Iterate through the list and check for valid odd numbers.
    for num in lst:
        if isinstance(num, int) and num > 0 and (num % 2) != 0:
            found_valid_odd = True
            # Square the number and add it to the result.
            result += num ** 2
    
    # If no valid odd numbers are found, return 0.
    if not found_valid_odd:
        return 0
    
    return result