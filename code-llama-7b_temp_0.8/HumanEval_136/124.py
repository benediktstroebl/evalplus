
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
    largest_smallest_integers_list = []
    for el in lst:
        if type(el) is int:
            if el < 0:
                largest_smallest_integers_list.append(el)
    if len(largest_smallest_integers_list) == 0:
        return (None, None)
    else:
        a = max(largest_smallest_integers_list)
        b = min(largest_smallest_integers_list)
        return (a, b)

