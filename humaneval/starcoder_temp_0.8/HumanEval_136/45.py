
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

    l = [n for n in lst if n < 0]
    p = [n for n in lst if n > 0]

    if l == []:
        a = None
    else:
        a = max(l)

    if p == []:
        b = None
    else:
        b = min(p)

    return (a, b)
