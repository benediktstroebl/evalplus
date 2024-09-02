
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
    result = None
    max_value = 0
    min_value = 0

    for num in lst:
        if num < 0:
            max_value = max(max_value, num)
            min_value = min(min_value, -num)
        elif num > 0:
            max_value = max(max_value, num)
            min_value = min(min_value, num)
        elif max_value is None and min_value is None:
            break
    if max_value is not None and min_value is not None:
        result = (max_value, min_value)
    return result
