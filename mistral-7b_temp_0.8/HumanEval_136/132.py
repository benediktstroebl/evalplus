
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

    # iterate through all elements in the array
    for i in lst:
        # if the current element is negative and its value is greater than the previous negative element
        if i < 0 and i > a:
            a = i
        # if the current element is positive and its value is smaller than the previous positive element
        elif i > 0 and i < b:
            b = i
    # return tuple
    if a is not None:
        return (a, b)
    else:
        return (None, None)
