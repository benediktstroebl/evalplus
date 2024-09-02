
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
    
    negatives = []
    positives = []
    
    for i in range(len(lst)):
        if lst[i] < 0:
            negatives.append(lst[i])
        else:
            positives.append(lst[i])
    
    negatives.sort(reverse=True)
    positives.sort()
    
    if len(negatives) == 0:
        return (None, None)
    
    return (negatives[0], positives[0])
    
    
    
    
