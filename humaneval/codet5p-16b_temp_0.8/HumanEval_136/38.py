
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

    if lst:
        neg = 0
        pos = 0
        for num in lst:
            if num < 0:
                neg = num
            elif num > 0:
                pos = num
            else:
                continue
        
        if neg == 0 and pos == 0:
            return (None, None)
        elif neg == 0:
            return (None, pos)
        elif pos == 0:
            return (neg, None)
        else:
            return (neg, pos)
    else:
        return (None, None)
