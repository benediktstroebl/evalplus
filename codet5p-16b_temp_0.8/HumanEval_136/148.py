
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

    max_negative, min_positive = None, None
    for integer in lst:
        if integer > 0:
            min_positive = integer
        if integer < 0:
            max_negative = integer
    if min_positive is None and max_negative is None:
        return None, None
    return max_negative, min_positive
