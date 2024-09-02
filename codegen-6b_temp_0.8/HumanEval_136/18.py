
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
    lst2 = [x for x in lst if x < 0]
    lst3 = [x for x in lst if x > 0]
    return (None, min(lst2)) if lst2 else (None, None)
    return (max(lst3), min(lst3)) if lst3 else (None, None)
