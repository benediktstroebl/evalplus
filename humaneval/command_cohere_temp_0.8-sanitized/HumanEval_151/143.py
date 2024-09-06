def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    Parameters:
        lst (list): A list of numbers.
    
    Returns:
        int: The sum of squares of odd integers that are non-negative and integers.
             If the list is empty, returns 0.
    """
    result = 0
    for num in lst:
        if num % 2 == 1 and num >= 0 and isinstance(num, int):
            result += num ** 2
    return result