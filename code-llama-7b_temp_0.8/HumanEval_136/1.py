
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

    # get list of negative integers
    negatives = [x for x in lst if x < 0]

    # get list of positive integers
    positives = [x for x in lst if x > 0]

    # check if any positive or negative integers exist
    if len(negatives) == 0 and len(positives) == 0:
        return (None, None)

    # check if there are positive integers
    if len(negatives) == 0:
        return (None, min(positives))

    # check if there are negative integers
    if len(positives) == 0:
        return (max(negatives), None)

    return (max(negatives), min(positives))
