
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
    l_largest = None
    l_smallest = None
    for x in lst:
        if x < 0:
            l_largest = x if l_largest is None or x < l_largest else l_largest
        if x > 0:
            l_smallest = x if l_smallest is None or x > l_smallest else l_smallest
    return (l_largest, l_smallest)

