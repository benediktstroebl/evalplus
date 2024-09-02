
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
    
    neg_largest = None
    pos_smallest = None
    for x in lst:
        if type(x) is int:
            if x < 0 and neg_largest == None:
                neg_largest = x
            if x < 0 and x > neg_largest:
                neg_largest = x
            if x > 0 and pos_smallest == None:
                pos_smallest = x
            if x > 0 and x < pos_smallest:
                pos_smallest = x
    return neg_largest, pos_smallest
