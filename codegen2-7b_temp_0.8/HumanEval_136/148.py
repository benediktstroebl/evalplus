
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
    positives = []
    negatives = []

    for x in lst:
        if x > 0:
            positives.append(x)
        elif x < 0:
            negatives.append(x)

    if positives:
        return sorted(positives)[-1], sorted(positives)[0]
    elif negatives:
        return sorted(negatives)[0], sorted(negatives)[-1]
    else:
        return None,
