
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
    lst_pos = find_pos(lst)
    lst_neg = find_neg(lst)
    lst_len = lst_pos + lst_neg
    if lst_len == 0:
        return (None, None)
    elif lst_len == 1:
        return (lst[0], lst[0])
    elif lst_pos == 0 and len(lst) == len(lst_neg):
        return (lst[0], lst[0])
    elif lst_neg == 0:
        return (lst[lst_pos], lst[0])
    elif lst_pos == 0:
        return (lst[0], lst[lst_neg])
    else:
        return (lst[lst_pos], lst[lst_neg])

