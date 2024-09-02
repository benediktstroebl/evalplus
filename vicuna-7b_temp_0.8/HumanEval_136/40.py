
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
    max_pos = []
    max_neg = []
    for num in lst:
        if num < 0:
            max_neg.append(max(max_neg) if max_neg else num)
        elif num > 0:
            max_pos.append(max(max_pos) if max_pos else num)
    return max_pos, max_neg
