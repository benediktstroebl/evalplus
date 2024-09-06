
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
    
    neg = []
    pos = []
    # Go through the list and if negative, add to neg list.
    # If positive, add to pos list.
    for n in lst:
        if n < 0:
            neg.append(n)
        elif n > 0:
            pos.append(n)
    
    # If there are no negative integers, return None
    if len(neg) == 0:
        neg = None
    else:
        # Otherwise return the max of negative integers
        neg = max(neg)
        
    # If there are no positive integers, return None
    if len(pos) == 0:
        pos = None
    else:
        # Otherwise return the min of the positive integers
        pos = min(pos)
        
    return neg, pos
