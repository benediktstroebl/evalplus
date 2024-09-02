
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
    if not lst:
        return None, None
    result = [None, None]
    for i in range(len(lst)):
        if lst[i] < 0:
            result[0] = lst[i]
        elif lst[i] > 0:
            result[1] = lst[i]
        if result[0] and result[1]:
            break
    return result
