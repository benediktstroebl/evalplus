
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

    if lst == []:
        return None, None
    else:
        lst_pos = [x for x in lst if x > 0]
        lst_neg = [x for x in lst if x < 0]
        if lst_neg == []:
            lst_neg = None
        if lst_pos == []:
            lst_pos = None

    return lst_neg, lst_pos
