def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    Parameters:
        lst (list): The input list of numbers.

    Returns:
        int: The sum of squares of odd integers that are non-negative and integers.
             If the list is empty or doesn't contain any eligible numbers, returns 0.
    """
    # Validate input: Check if the input list is empty or all negative
    if not lst or all(n < 0 for n in lst):
        return 0
    
    # Filter eligible numbers, square them, and sum up
    return sum(int(n)**2 for n in lst if n % 2 and isinstance(n, int))