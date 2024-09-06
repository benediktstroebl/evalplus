
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

    if len(lst) == 1:
        return lst[0]

    lst_pos = list(filter(lambda x: x > 0, lst))
    lst_neg = list(filter(lambda x: x < 0, lst))

    if len(lst_pos) == 0:
        return None, None

    if len(lst_neg) == 0:
        return None, lst_pos[0]

    return lst_neg[-1], lst_pos[0]




