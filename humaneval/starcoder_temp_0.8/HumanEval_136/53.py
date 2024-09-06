
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
    negatives = []
    positives = []
    for i in lst:
        if i < 0:
            negatives.append(i)
        if i > 0:
            positives.append(i)
    if len(negatives) == 0:
        negatives = None
    if len(positives) == 0:
        positives = None
    return (negatives, positives)
