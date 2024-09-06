
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
    elif len(lst) == 1:
        if lst[0] < 0:
            return (None, lst[0])
        else:
            return (lst[0], None)
    
    negatives = []
    positives = []
    
    for item in lst:
        if item < 0:
            negatives.append(item)
        elif item > 0:
            positives.append(item)
            
    if len(negatives) > 0:
        return (max(negatives), min(positives))
    elif len(positives) > 0:
        return (max(positives), min(positives))
    else:
        return (None, None)
        
        
