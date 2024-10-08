
def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    '''
    return (None, None) if len(lst) == 0 else (max(filter(lambda x: x < 0, lst)), min(filter(lambda x: x > 0, lst)))

assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (1, 7)
assert largest_smallest_integers([]) == (None, None)
assert largest_smallest_integers([0]) == (None, None)
assert largest_smallest_integers([-5, -6, -7, -8, -6]) == (None, None)
assert largest_smallest_integers([]) == (None, None)
