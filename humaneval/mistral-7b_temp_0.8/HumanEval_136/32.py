
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

    lst = sorted(lst)
    if len(lst) == 0:
        return None, None
    else:
        if all(i >= 0 for i in lst):
            return None, lst[0]
        elif all(i < 0 for i in lst):
            return lst[-1], None
        else:
            return lst[-1], lst[0]
