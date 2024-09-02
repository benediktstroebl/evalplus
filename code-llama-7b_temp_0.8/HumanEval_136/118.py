
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
    maximum = None
    minimum = None
    for i in lst:
        if type(i) != int:
            continue
        elif i < 0:
            if maximum is None:
                maximum = i
            elif maximum < i:
                maximum = i
        elif i > 0:
            if minimum is None:
                minimum = i
            elif minimum > i:
                minimum = i
    return maximum, minimum
