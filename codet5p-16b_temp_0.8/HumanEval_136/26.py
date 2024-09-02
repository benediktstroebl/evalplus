
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

    result = []
    if lst:
        for item in lst:
            if item < 0:
                result.append(item)
            else:
                result.append(item)
        result.sort()
        result.reverse()
        result.append(result[0])
        result.pop(0)
        return (None, None) if not result else (result[0], result[1])
    else:
        return (None, None)
