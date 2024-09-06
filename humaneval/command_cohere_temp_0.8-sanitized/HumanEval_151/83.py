def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    Returns:
        int: The sum of squares of odd positive integers.
    """
    odd_sq = sum(x**2 for x in lst if x % 2 != 0 and x >= 0)
    return int(odd_sq)