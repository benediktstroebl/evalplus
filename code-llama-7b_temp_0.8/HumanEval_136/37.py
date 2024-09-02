
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
    if not lst:
        return (None, None)

    largest_neg_int = None
    smallest_pos_int = None

    for num in lst:
        if isinstance(num, int) and num < 0:
            if largest_neg_int is None:
                largest_neg_int = num
            elif num > largest_neg_int:
                largest_neg_int = num

        elif isinstance(num, int) and num > 0:
            if smallest_pos_int is None:
                smallest_pos_int = num
            elif num < smallest_pos_int:
                smallest_pos_int = num

    return (largest_neg_int, smallest_pos_int)

