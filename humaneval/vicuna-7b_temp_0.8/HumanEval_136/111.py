
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
    if not lst:
        return None, None

    lst.reverse()
    max_negative = -1
    min_positive = max_negative

    for x in lst:
        if x >= 0:
            max_positive = max(max_positive, x)
        elif x < 0:
            min_negative = min(min_negative, x)

    return max_positive, min_negative
