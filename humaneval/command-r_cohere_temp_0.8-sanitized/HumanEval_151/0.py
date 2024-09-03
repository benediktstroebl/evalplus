def double_the_difference(lst):
    '''
    Calculates the sum of squares of odd integers in the list, ignoring negative numbers and non-integers.

    Args:
        lst (list): A list of integers.

    Returns:
        int: Sum of squares of odd numbers or 0 if the list is empty.
    '''
    return sum(x**2 for x in lst if x > 0 and isinstance(x, int) and x % 2 != 0) or 0