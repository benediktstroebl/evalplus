
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

    positive_integers = []
    negative_integers = []
    result = []
    for x in lst:
        if isinstance(x, int):
            if x >= 0:
                positive_integers.append(x)
            elif x < 0:
                negative_integers.append(x)
            else:
                continue
        else:
            continue
    if negative_integers:
        result.append(min(negative_integers))
    else:
        result.append(None)
    if positive_integers:
        result.append(max(positive_integers))
    else:
        result.append(None)
    return tuple(result)

