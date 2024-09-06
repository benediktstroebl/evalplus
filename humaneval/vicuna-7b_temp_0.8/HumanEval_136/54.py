
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
    # The first element is the largest negative integer
    largest_negative = max(lst)
    if largest_negative == 0:
        return None, None
    elif largest_negative == -1:
        return largest_negative, None
    elif largest_negative == -2:
        return largest_negative-1, None
    else:
        largest_negative -= 1
        # The last element is the smallest positive integer
        smallest_positive = min(lst)
        if smallest_positive == 0:
            return None, smallest_positive
        elif smallest_positive == 1:
            return largest_negative, smallest_positive
        elif smallest_positive == 2:
            return largest_negative, smallest_positive-1
        else:
            return largest_negative, smallest_positive
