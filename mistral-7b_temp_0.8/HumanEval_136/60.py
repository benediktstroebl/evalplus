
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

    n_lst = []

    for i in lst:
        if i >= 0:
            n_lst.append(i)
        else:
            n_lst.append(-i)

    if len(n_lst) == 0:
        return None, None

    largest_smallest = (max(n_lst), min(n_lst))
    largest_smallest = (None, None) if largest_smallest == (0, 0) else largest_smallest
    return largest_smallest[0] * (-1), largest_smallest[1]
