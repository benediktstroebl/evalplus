
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
    negative = []
    positive = []
    for i in lst:
        if i < 0:
            negative.append(i)
        else:
            positive.append(i)
    negative = sorted(negative)
    positive = sorted(positive)
    if len(negative) == 0:
        neg_val = None
    else:
        neg_val = negative[0]
    if len(positive) == 0:
        pos_val = None
    else:
        pos_val = positive[0]
    return (neg_val, pos_val)
    