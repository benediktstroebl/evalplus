
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
    # Solution
    integers = [integer for integer in lst if isinstance(integer, int)]
    if len(integers) == 0:
        return (None, None)
    negative_integers = sorted([integer for integer in integers if integer < 0])
    positive_integers = sorted([integer for integer in integers if integer > 0])
    if negative_integers:
        largest_negative = negative_integers[-1]
    else:
        largest_negative = None
    if positive_integers:
        smallest_positive = positive_integers[0]
    else:
        smallest_positive = None
    return (largest_negative, smallest_positive)
    
    # My first try
    # largest_n = None
    # smallest_p = None
    # for item in lst:
    #     if isinstance(item, int) and item < 0:
    #         largest_n = item
    #     elif isinstance(item, int) and item > 0:
    #         smallest_p = item
    # return (largest_n, smallest_p)
    # Using lambda functions
    # largest_n = max(filter(lambda x: x < 0, lst), default = None)
    # smallest_p = min(filter(lambda x: x > 0, lst), default = None)
    # return (largest_n, smallest_p)
    
    
