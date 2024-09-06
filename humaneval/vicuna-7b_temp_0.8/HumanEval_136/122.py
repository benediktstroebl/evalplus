
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
    for i in lst:
        if i < 0:
            max_lst = lst
            max_val = i
        elif i > 0:
            min_lst = lst
            min_val = i
        else:
            max_lst = lst
            max_val = max(lst)
            min_lst = lst
            min_val = min(lst)
    return (max_val, min_val)
