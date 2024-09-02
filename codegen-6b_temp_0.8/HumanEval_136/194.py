
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
    result = [None, None]
    for x in lst:
        #if '-' not in x:
        if type(x) != int:
            continue
        if result[0] is None:
            if x < 0:
                result[0] = x
            elif x > 0:
                result[1] = x
        else:
            if x < 0 and x > result[0]:
                result[0] = x
            elif x > 0 and x < result[1]:
                result[1] = x
    if result[0] is None:
        return result
    return (result[0], result[1])
