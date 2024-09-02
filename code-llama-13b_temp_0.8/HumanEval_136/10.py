
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
    negative_int, positive_int = None, None
    for x in lst:
        if x < 0:
            if negative_int is None:
                negative_int = x
            elif x > negative_int:
                negative_int = x
        if x > 0:
            if positive_int is None:
                positive_int = x
            elif x < positive_int:
                positive_int = x
    return negative_int, positive_int
    
