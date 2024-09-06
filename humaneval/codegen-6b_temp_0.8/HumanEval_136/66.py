
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
    for a in lst:
        if a < 0:
            if negative is None or a > negative:
                negative = a
        if a > 0:
            if positive is None or a < positive:
                positive = a
    return (negative, positive)
