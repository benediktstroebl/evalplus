
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
    # Your code here
    res = [x for x in lst if x < 0]
    res2 = [x for x in lst if x >= 0]
    res3 = [x for x in lst if x == 0]
    if len(res) == 0:
        res = None
    else:
        res = max(res)
    if len(res2) == 0:
        res2 = None
    else:
        res2 = min(res2)
    return (res, res2)
