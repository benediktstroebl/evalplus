
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
    # first remove anything that is not an int
    lst_copy = []
    for number in lst:
        if isinstance(number, int):
            lst_copy.append(number)
    if len(lst_copy) == 0:
        return None, None
    # sort list
    lst_copy.sort()
    if lst_copy[0] < 0:
        return lst_copy[0], lst_copy[0 + 1]
    if len(lst_copy) > 0:
        return None, lst_copy[0]
    return None, None

    '''
    Other solution.
    a = max(filter(lambda x: x < 0, lst))
    b = min(filter(lambda x: x > 0, lst))
    return (a, b)
    '''
