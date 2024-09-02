
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

    # Solution 1:
    # a = max([num for num in lst if num < 0])
    # b = min([num for num in lst if num >= 0])
    # return (a, b)

    # Solution 2:
    a = b = None
    for num in lst:
        if a is None and num < 0:
            a = num
        elif num < a:
            a = num
    for num in lst:
        if b is None and num >= 0:
            b = num
        elif num < b:
            b = num
    return (a, b)

