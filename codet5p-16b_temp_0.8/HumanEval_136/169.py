
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

    max_num = None
    min_num = None

    for i in lst:
        if i > 0:
            if min_num == None:
                min_num = i
            else:
                min_num = min(i, min_num)
        else:
            if max_num == None:
                max_num = i
            else:
                max_num = max(i, max_num)
    return max_num, min_num
