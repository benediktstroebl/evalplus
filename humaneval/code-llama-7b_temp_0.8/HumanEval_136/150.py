
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
    max_pos, min_neg = None, None
    for num in lst:
        if isinstance(num, int):
            if num < 0:
                if (not min_neg) or num < min_neg:
                    min_neg = num
            elif num > 0:
                if (not max_pos) or num > max_pos:
                    max_pos = num
    return min_neg, max_pos
