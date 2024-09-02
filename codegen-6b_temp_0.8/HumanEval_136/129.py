
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
    negative_positive = []
    negative_negative = []

    for i in lst:
        if i < 0:
            negative_negative.append(i)
        elif i > 0:
            negative_positive.append(i)
        else:
            negative_negative.append(i)

    if len(negative_negative) > 0:
        return (max(negative_negative), min(negative_negative))
    elif len(negative_positive) > 0:
        return (max(negative_positive), min(negative_positive))
    else:
        return (None, None)

