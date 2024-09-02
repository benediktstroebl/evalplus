
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
    return_dict = {}
    for item in lst:
        if item < 0:
            try:
                if item > return_dict['a']:
                    return_dict['a'] = item
            except KeyError:
                return_dict['a'] = item
        elif item > 0:
            try:
                if item < return_dict['b']:
                    return_dict['b'] = item
            except KeyError:
                return_dict['b'] = item
        else:
            continue
    if len(return_dict) == 2:
        return (return_dict['a'], return_dict['b'])
    elif len(return_dict) == 1:
        if 'a' in return_dict:
            return (return_dict['a'], None)
        elif 'b' in return_dict:
            return (None, return_dict['b'])
    else:
        return (None, None)
