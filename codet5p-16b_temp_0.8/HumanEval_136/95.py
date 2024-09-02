
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

    negative = [str(i) for i in lst if i < 0]
    positive = [str(i) for i in lst if i >= 0]
    if negative:
        a = max([int(i) for i in negative])
    else:
        a = None
    if positive:
        b = min([int(i) for i in positive])
    else:
        b = None
    return a, b
    
    
