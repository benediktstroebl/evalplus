
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
    # 1. Sort the list of integers, and set the variables.
    integers = sorted([int(i) for i in lst])
    smallest_positive = None
    largest_negative = None
    
    # 2. Set the variables.
    if integers:
        smallest_positive = integers[0] if integers[0] > 0 else None
        largest_negative = integers[-1] if integers[-1] < 0 else None
    
    # 3. Return the tuple.
    return (largest_negative, smallest_positive)
