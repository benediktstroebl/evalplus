
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
    result = [None, None]
    for el in lst:
        if type(el) == int:
            if el > 0:
                if result[1] == None or el < result[1]:
                    result[1] = el
            if el < 0:
                if result[0] == None or el > result[0]:
                    result[0] = el
    return tuple(result)

