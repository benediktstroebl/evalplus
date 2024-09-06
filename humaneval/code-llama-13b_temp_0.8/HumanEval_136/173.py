
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
    
    positive_lst = [i for i in lst if i > 0]
    if not positive_lst:
        return (None, None)
    
    negative_lst = [i for i in lst if i < 0]
    if not negative_lst:
        return (None, positive_lst[0])
    
    return (negative_lst[0], positive_lst[0])
    
