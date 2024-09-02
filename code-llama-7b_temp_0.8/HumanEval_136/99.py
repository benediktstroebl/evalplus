
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
    lst = filter(lambda x: isinstance(x, int), lst)
    lst = sorted(lst)
    if lst == []:
        return (None, None)
    else:
        neg_vals = [x for x in lst if x < 0]
        pos_vals = [x for x in lst if x > 0]
        if len(neg_vals) == 0:
            neg_vals = None
        else:
            neg_vals = neg_vals[-1]
        if len(pos_vals) == 0:
            pos_vals = None
        else:
            pos_vals = pos_vals[0]
        return (neg_vals, pos_vals)

