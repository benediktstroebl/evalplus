
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
    return_tuple = []

    if lst:
        for i in lst:
            if i < 0:
                return_tuple.append(i)
        if return_tuple:
            return_tuple.sort()
            return_tuple.reverse()
            return_tuple = tuple(return_tuple)
            if len(return_tuple) > 0:
                return_tuple = (return_tuple[0], None)
            else:
                return_tuple = (None, None)
        else:
            return_tuple.append(None)
            return_tuple.append(None)
            return_tuple = tuple(return_tuple)

        for i in lst:
            if i > 0:
                return_tuple.append(i)
        if return_tuple:
            return_tuple.sort()
            return_tuple = tuple(return_tuple)
            if len(return_tuple) > 0:
                return_tuple = (None, return_tuple[0])
            else:
                return_tuple = (None, None)
        else:
            return_tuple.append(None)
            return_tuple.append(None)
            return_tuple = tuple(return_tuple)

        return return_tuple
    else:
        return_tuple.append(None)
        return_tuple.append(None)
        return_tuple = tuple(return_tuple)
        return return_tuple
