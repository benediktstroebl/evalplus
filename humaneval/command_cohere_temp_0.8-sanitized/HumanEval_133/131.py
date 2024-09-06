def sum_squares(lst):
    """
    Return the sum of squared integers in the list.
    
    >>> sum_squares([1, 2, 3])
    14
    >>> sum_squares([1, 4, 9])
    98
    >>> sum_squares([1, 3, 5, 7])
    84
    >>> sum_squares([1.4, 4.2, 0])
    29
    >>> sum_squares([-2.4, 1, 1])
    6
    >>> sum_squares([0, 0, 0, 0, 0, 0, 0, 7])
    497
    >>> sum_squares([-3, -2, -1, 0, 0, 1, 2, 3])
    30
    """
    result = 0
    # Use list comprehension to square each number and filter out non-integer values
    for num in lst:
        result += int(num ** 2 if isinstance(num, (int, float)) else 0)
    return result