
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
    if len(lst) > 0:
        positive = [x for x in lst if x > 0]
        negative = [x for x in lst if x < 0]

        if len(positive) > 0:
            smallest_pos = min(positive)
        else:
            smallest_pos = None
        if len(negative) > 0:
            largest_neg = max(negative)
        else:
            largest_neg = None
        return largest_neg, smallest_pos
    else:
        return None, None




