
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
    # if not lst:
    #     return None, None
    
    # for integer in lst:
    #     if integer < 0:
    #         negative_integer = integer
    #     if integer > 0:
    #         positive_integer = integer
    # return negative_integer, positive_integer
    
    return (max(filter(lambda x: x < 0, lst)) if any(x < 0 for x in lst) else None, 
            min(filter(lambda x: x > 0, lst)) if any(x > 0 for x in lst) else None)

