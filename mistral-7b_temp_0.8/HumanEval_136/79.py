
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
    if lst == []:
        return None, None
    elif lst[0] < 0:
        a = lst[0]
        lst = lst[1:]
        if lst == []:
            return a, None
    elif lst[-1] > 0:
        b = lst[-1]
        lst = lst[:-1]
        if lst == []:
            return None, b
    return largest_smallest_integers(lst)


