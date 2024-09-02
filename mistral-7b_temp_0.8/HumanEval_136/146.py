
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

    largest_neg = None
    smallest_pos = None

    for num in lst:
        if num > 0 and smallest_pos == None:
            smallest_pos = num
        elif num > 0:
            if num < smallest_pos:
                smallest_pos = num

        if num < 0 and largest_neg == None:
            largest_neg = num
        elif num < 0:
            if num > largest_neg:
                largest_neg = num

    if largest_neg == None and smallest_pos == None:
        return None, None
    else:
        return largest_neg, smallest_pos

