
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

    lst_sorted = sorted(lst)
    if not lst_sorted:
        return (None, None)
    a = None
    b = None
    if lst_sorted[0] < 0:
        a = lst_sorted[0]
    if lst_sorted[-1] > 0:
        b = lst_sorted[-1]
    return (a, b)

