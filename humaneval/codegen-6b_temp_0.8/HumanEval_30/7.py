

def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    # Hint: you can use a for loop on a list to get positive numbers
    # without the help of any function, or use while loop to get positive numbers
    # without the help of any function.
    return [num for num in l if num > 0]
