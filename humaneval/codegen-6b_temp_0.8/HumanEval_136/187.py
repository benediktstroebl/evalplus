
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
    lst_pos = [x for x in lst if x > 0]
    lst_neg = [x for x in lst if x < 0]
    if lst_pos == []:
        if lst_neg == []:
            return (None, None)
        return (max(lst_neg), min(lst_neg))
    if lst_neg == []:
        return (max(lst_pos), min(lst_pos))
    return (max(lst_neg), min(lst_pos))
