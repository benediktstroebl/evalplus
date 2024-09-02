
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

    # Finding the largest negative number
    lst.sort()
    if lst[0] >= 0:
        a = None
    else:
        a = lst[0]

    # Finding the smallest positive number
    if lst[-1] <= 0:
        b = None
    else:
        b = lst[-1]

    return (a, b)

