
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

    max_int = None
    min_int = None

    for i in range(len(lst)):
        if lst[i] < 0:
            if max_int == None:
                max_int = lst[i]
            elif lst[i] > max_int:
                max_int = lst[i]
        if lst[i] > 0:
            if min_int == None:
                min_int = lst[i]
            elif lst[i] < min_int:
                min_int = lst[i]

    return (max_int, min_int)
