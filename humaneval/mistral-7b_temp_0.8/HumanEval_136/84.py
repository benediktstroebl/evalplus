
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
    neg = None
    pos = None
    for number in lst:
        if number < 0:
            if neg is None:
                neg = number
            elif neg > number:
                neg = number
        elif number > 0:
            if pos is None:
                pos = number
            elif pos < number:
                pos = number

    if neg is None:
        return None, None
    elif pos is None:
        return neg, None
    else:
        return neg, pos
