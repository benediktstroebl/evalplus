
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
    a = None
    b = None
    for x in lst:
        if x < 0:
            largest = lst.index(max(lst, key=lst.index))
            b = x
            a = max(lst)
        elif x > 0:
            smallest = lst.index(min(lst, key=lst.index))
            a = min(lst)
            b = x
    return a, b
