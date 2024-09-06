
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
    maxi = None
    mini = None
    for el in lst:
        if type(el) is int:
            if el < 0:
                if maxi is None or el > maxi:
                    maxi = el
            if el >= 0:
                if mini is None or el < mini:
                    mini = el
    return maxi, mini

