
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

    neg_lst = [item for item in lst if type(item) == int and item < 0]
    pos_lst = [item for item in lst if type(item) == int and item >= 0]
    
    # If list is empty or there is no negative and/or positive integers.
    if neg_lst == [] and pos_lst == []:
        return (None, None)
    
    elif neg_lst == []:
        return (None, sorted(pos_lst)[0])
        
    elif pos_lst == []:
        return (sorted(neg_lst)[-1], None)
    
    return (sorted(neg_lst)[-1], sorted(pos_lst)[0])
    
