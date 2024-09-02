
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
    results = []
    for item in lst:
        if item >= 0:
            results.append(item)
        elif item < 0:
            results.append(item)

    if len(results) == 0:
        return (None, None)
    elif len(results) == 1:
        return (results[0], None)
    else:
        max_result = max(results)
        min_result = min(results)
        return (max_result, min_result)


