
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
    for i in lst:
        if i < 0:
            negative = i if negative is None or negative > i else negative
        else:
            positive = i if positive is None or positive < i else positive
    if negative is None:
        return (None, None)
    elif positive is None:
        return (negative, None)
    else:
        return (negative, positive)
