
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
        return (None, None)
    negative_max = negative_min = None
    positive_max = positive_min = None
    for num in lst:
        if num < 0:
            if negative_max is None or negative_max < num:
                negative_max = num
        elif num > 0:
            if positive_max is None or positive_max > num:
                positive_max = num
        else:
            continue
    return (negative_max, positive_min)
