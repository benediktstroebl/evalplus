
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

    largest_neg_int = None
    smallest_pos_int = None
    neg_int_pos_int_tuple = (largest_neg_int, smallest_pos_int)
    for num in lst:
        if largest_neg_int is None:
            if num < 0:
                largest_neg_int = num
        else:
            if num < 0:
                if largest_neg_int < num:
                    largest_neg_int = num
            else:
                if smallest_pos_int is None:
                    smallest_pos_int = num
                else:
                    if smallest_pos_int > num:
                        smallest_pos_int = num
    neg_int_pos_int_tuple = (largest_neg_int, smallest_pos_int)
    return neg_int_pos_int_tuple
