
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
    largest_neg, smallest_pos = None, None
    for item in lst:
        if isinstance(item, int):
            if item < 0 and (largest_neg is None or item > largest_neg):
                largest_neg = item
            elif item > 0 and (smallest_pos is None or item < smallest_pos):
                smallest_pos = item
    return largest_neg, smallest_pos

