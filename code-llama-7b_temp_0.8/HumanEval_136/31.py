
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
    # your code here
    min_pos = None
    max_neg = None
    for item in lst:
        if item < 0:
            max_neg = item if item > max_neg else max_neg
        elif item > 0:
            min_pos = item if item < min_pos else min_pos
        else:
            continue
    return (max_neg, min_pos)
