
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
    positive_ints = []
    negative_ints = []
    for item in lst:
        if isinstance(item, int):
            if item >= 0:
                positive_ints.append(item)
            else:
                negative_ints.append(item)
        else:
            continue
    if len(negative_ints) == 0:
        a = None
    else:
        a = max(negative_ints)
    if len(positive_ints) == 0:
        b = None
    else:
        b = min(positive_ints)

    return a, b
















