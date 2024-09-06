
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
    largest_neg = 0
    largest_pos = 0
    neg_found = False
    pos_found = False

    for num in lst:
        if num < 0:
            if neg_found == False:
                neg_found = True
                largest_neg = num
            else:
                if num > largest_neg:
                    largest_neg = num
        elif num > 0:
            if pos_found == False:
                pos_found = True
                largest_pos = num
            else:
                if num < largest_pos:
                    largest_pos = num

    if neg_found == False:
        return None, None
    else:
        return largest_neg, largest_pos













































































