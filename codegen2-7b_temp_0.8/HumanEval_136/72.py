
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
        return None, None
    
    max_lst = []
    min_lst = []
    
    for x in lst:
        if x < 0:
            max_lst.append(x)
        else:
            min_lst.append(x)
            
    if len(max_lst) > len(min_lst):
        return max_lst, min_lst
    else:
        return min_lst, max_l
