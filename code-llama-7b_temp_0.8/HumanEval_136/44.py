
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
    if lst:
        i = 0
        while i < len(lst):
            if i >= 0:
                if lst[i] > lst[result[0]]:
                    result[0] = i
                elif lst[i] < lst[result[1]]:
                    result[1] = i
            i += 1
    return tuple(result)



