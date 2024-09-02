
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
    # Your code here

    if len(lst) == 0:
        return None, None

    largest_neg = None
    smallest_pos = None

    for el in lst:
        if el < 0:
            if largest_neg is None:
                largest_neg = el
            elif el > largest_neg:
                largest_neg = el
        elif el > 0:
            if smallest_pos is None:
                smallest_pos = el
            elif el < smallest_pos:
                smallest_pos = el

    if largest_neg is None:
        return None, smallest_pos
    else:
        return largest_neg, smallest_pos
