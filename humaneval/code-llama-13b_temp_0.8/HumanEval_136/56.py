
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
    smallest_positive = None
    largest_negative = None
    for x in lst:
        if type(x) is not int:
            continue
        if smallest_positive is None and x > 0:
            smallest_positive = x
        elif smallest_positive and x > 0 and smallest_positive > x:
            smallest_positive = x
        if largest_negative is None and x < 0:
            largest_negative = x
        elif largest_negative and x < 0 and largest_negative < x:
            largest_negative = x
    return (largest_negative, smallest_positive)

