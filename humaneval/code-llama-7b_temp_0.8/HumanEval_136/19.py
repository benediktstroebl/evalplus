
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
    result = []
    for i in lst:
        if i < 0:
            result.append(i)
    result2 = []
    for i in lst:
        if i > 0:
            result2.append(i)
    if len(result) == 0:
        return None, min(result2)
    elif len(result2) == 0:
        return max(result), None
    else:
        return max(result), min(result2)


