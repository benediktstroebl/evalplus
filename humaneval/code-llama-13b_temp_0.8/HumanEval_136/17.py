
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
        return None, None
    
    positive = None
    negative = None
    for item in lst:
        if isinstance(item, int) and item < 0:
            if negative is None or negative < item:
                negative = item
        if isinstance(item, int) and item > 0:
            if positive is None or positive > item:
                positive = item
    return negative, positive
