
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

    min_lst = []
    max_lst = []
    for x in lst:
        if x < 0:
            min_lst.append(x)
        else:
            max_lst.append(x)
    if min_lst:
        min_lst = max(min_lst)
    else:
        min_lst = None
    if max_lst:
        max_lst = min(max_lst)
    else:
        max_lst = None
    return (min_lst, max_lst)
