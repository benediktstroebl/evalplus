

def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [x for x in l if x > 0]

'''
Goal:
Is there a way to get the first n elements of a list?
>>> [1, 2, 3, 4, 5, 6, 7]

>>> lst = [1, 2, 3, 4, 5, 6, 7]
>>> lst[:3]

SyntaxError: invalid syntax

'''