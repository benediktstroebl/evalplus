def double_the_difference(lst):
    """
    Returns the sum of squares of odd integers in the list, whilst 
    ignoring non-integer values and negative numbers. Empty list returns 0.
    
    Args:
        lst (list): List of numbers.
    
    Returns:
        int: Sum of squares of odd integers or 0.
    """
    msg = 'Initial list: {}' .format(lst)
    print(msg)  # Print list for inspection
    result = 0
    # Filter only odd integers and validate them
    odd_and_valid = [num for num in lst if num % 2 != 0 and isinstance(num, int) and num >= 0]
    if not odd_and_valid:
        return 0  # Empty list, return 0
    msg = 'Filtered list with odd, non-negative, integer numbers: {}' .format(odd_and_valid)
    print(msg)  # Print filtered list for inspection
    # Calculate the sum of squares for the valid odd numbers
    for num in odd_and_valid:
        result += num ** 2
    return result