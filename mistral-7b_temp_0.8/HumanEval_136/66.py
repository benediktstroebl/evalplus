
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

    lst_pos = [i for i in lst if i > 0]
    lst_neg = [i for i in lst if i < 0]

    if lst_pos and lst_neg:
        a = max(lst_neg)
        b = min(lst_pos)
        return a, b
    elif lst_pos:
        b = min(lst_pos)
        return b, None
    elif lst_neg:
        a = max(lst_neg)
        return a, None
    else:
        return None, None

