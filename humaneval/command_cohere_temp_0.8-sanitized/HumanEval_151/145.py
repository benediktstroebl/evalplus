def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    """
    if not lst:
        return 0
    
    result = 0
    for num in lst:
        if isinstance(num, int) and num % 2:
            result += num ** 2
    return result