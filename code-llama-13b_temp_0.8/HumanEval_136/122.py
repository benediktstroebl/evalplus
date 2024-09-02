
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
        return (None, None)
    
    positive = None
    negative = None
    for integer in lst:
        if integer < 0:
            if negative is None:
                negative = integer
            else:
                negative = max(negative, integer)
        elif integer > 0:
            if positive is None:
                positive = integer
            else:
                positive = min(positive, integer)
    
    return (negative, positive)
