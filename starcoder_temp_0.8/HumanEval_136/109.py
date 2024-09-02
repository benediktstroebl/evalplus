
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
    max_neg = None
    min_pos = None
    for item in lst:
        if item < 0:
            if max_neg is None or max_neg < item:
                max_neg = item
        elif item > 0:
            if min_pos is None or min_pos > item:
                min_pos = item

    return (max_neg, min_pos)

