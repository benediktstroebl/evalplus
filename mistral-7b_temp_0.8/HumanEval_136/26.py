
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
    if len(lst) == 0:
        return None, None
    max_value = float('-inf')
    min_value = float('inf')
    for i in lst:
        if i < 0:
            if i > max_value:
                max_value = i
        elif i > 0:
            if i < min_value:
                min_value = i
    if max_value == float('-inf'):
        return None, None
    return max_value, min_value

