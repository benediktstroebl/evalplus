
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
    # return (None, None) if list is empty or if there are no positive or negative integers
    if not lst or (max(lst) * min(lst)) > 0:
        return (None, None)
    
    # create a list of negative integers and positive integers
    negative_int = []
    positive_int = []
    for n in lst:
        if n < 0:
            negative_int.append(n)
        elif n > 0:
            positive_int.append(n)
            
    # return the tuple
    return (max(negative_int), min(positive_int))
