
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
    # No need for extra space, just go through the list and check if negative or positive integers, and update the min/max as needed
    neg_int = None
    pos_int = None
    for x in lst:
        if x < 0 and (neg_int == None or neg_int < x):
            neg_int = x
        elif x > 0 and (pos_int == None or pos_int > x):
            pos_int = x
    
    return (neg_int, pos_int)
