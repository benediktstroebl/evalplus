
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
    large = small = lst[0]
    for el in lst:
        if large < el and isinstance(el, int):
            large = el
        elif small > el and isinstance(el, int):
            small = el
    return (None, small) if large < 0 else (large, None) if small > 0 else (None, None)
    
