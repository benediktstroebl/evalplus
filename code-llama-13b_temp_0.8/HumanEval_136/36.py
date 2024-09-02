
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
    list_negative = []
    list_positive = []
    for n in lst:
        if n <= 0:
            list_negative.append(n)
        elif n >= 0:
            list_positive.append(n)
    if list_negative and list_positive:
        return max(list_negative), min(list_positive)
    return None, None
    
    
