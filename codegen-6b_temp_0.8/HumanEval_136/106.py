
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
    from numpy import array
    lst = array(lst)
    r = lst.argsort()
    response = None, None
    if lst.size == 0:
        return response
    else:
        smallest = r[0]
        for i in r[1:]:
            if lst[i] < largest:
                smallest = i
        response = smallest, lst[smallest]
        return response
