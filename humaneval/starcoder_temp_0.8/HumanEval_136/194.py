
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
    if len(lst) == 0:
        return None, None

    largest_negative = 0
    smallest_positive = 0

    for i in lst:
        if i < 0:
            if i < largest_negative:
                largest_negative = i
        elif i > 0:
            if smallest_positive == 0:
                smallest_positive = i
            elif i > smallest_positive:
                smallest_positive = i

    if largest_negative == 0:
        largest_negative = None

    if smallest_positive == 0:
        smallest_positive = None

    return largest_negative, smallest_positive
