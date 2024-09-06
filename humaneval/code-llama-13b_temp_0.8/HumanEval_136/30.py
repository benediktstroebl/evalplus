
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
    large = negative = smallest = None
    for i in lst:
        if isinstance(i, int) and i < 0:
            if negative is None or negative < i:
                negative = i
        elif isinstance(i, int) and i > 0:
            if large is None or large < i:
                large = i
            if smallest is None or smallest > i:
                smallest = i
    return large, smallest

