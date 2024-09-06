
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
    negative = None
    positive = None

    for n in lst:
        if n < 0:
            negative = n
        elif n > 0:
            positive = n

    if negative is None and positive is None:
        return (None, None)
    elif negative is None:
        return (positive, None)
    elif positive is None:
        return (negative, None)
    else:
        return (negative, positive)

assert largest_smallest_integers([1, -2, 3]) == (None, -2)
assert largest_smallest_integers([-2, 0, 3]) == (None, 0)
assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (1, -2)
assert largest_smallest_integers([]) == (None, None)
assert largest_smallest_integers([0, -2, 3]) == (None, -2)
assert largest_smallest_integers([-2, 0]) == (None, 0)
