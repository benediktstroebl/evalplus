
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
    min_num, max_num = None, None
    for i in lst:
        if (i < 0) and ((min_num is None) or (i < min_num)):
            min_num = i
        if (i > 0) and ((max_num is None) or (i > max_num)):
            max_num = i
    return min_num, max_num

