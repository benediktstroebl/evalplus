
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
    ints = [x for x in lst if type(x) == int]
    pos = [x for x in ints if x > 0]
    neg = [x for x in ints if x < 0]
    if pos:
        return (None, min(pos))
    if neg:
        return (max(neg), None)
    return (None, None)

    
