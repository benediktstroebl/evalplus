
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
    if len(lst) == 0:
        return (None, None)
    max_negative = None
    min_positive = None
    for item in lst:
        if item < 0:
            if max_negative == None:
                max_negative = item
            else:
                max_negative = max(max_negative, item)
        else:
            if min_positive == None:
                min_positive = item
            else:
                min_positive = min(min_positive, item)
    return (max_negative, min_positive)

