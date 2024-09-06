
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
    if len(lst) == 0:
        return (None, None)
    
    lst_copy = lst[:]
    lst_copy.sort()
    
    if lst_copy[0] < 0:
        largest_negative = lst_copy[-1]
    else:
        largest_negative = None
    
    if lst_copy[-1] > 0:
        smallest_positive = lst_copy[0]
    else:
        smallest_positive = None
    
    return (largest_negative, smallest_positive)
