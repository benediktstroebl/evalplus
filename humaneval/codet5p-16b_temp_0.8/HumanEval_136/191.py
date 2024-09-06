
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

    max1 = None
    min1 = None
    for i in lst:
        if i > 0 and (min1 is None or min1 > i):
            min1 = i
        if i < 0 and (max1 is None or max1 < i):
            max1 = i

    return (max1, min1)

