
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
        return (None, None)
    else:
        negatives = []
        positives = []
        for item in lst:
            if item < 0:
                negatives.append(item)
            elif item > 0:
                positives.append(item)
        return (max(negatives) if len(negatives) > 0 else None,
                min(positives) if len(positives) > 0 else None)
