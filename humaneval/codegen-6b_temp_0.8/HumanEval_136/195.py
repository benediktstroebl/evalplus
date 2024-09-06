
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
    negatives = [integer for integer in lst if integer < 0]
    positives = [integer for integer in lst if integer > 0]
    if len(negatives) > 0 and len(positives) > 0:
        return (max(negatives), min(positives))
    elif len(negatives) > 0:
        return (max(negatives), None)
    elif len(positives) > 0:
        return (None, min(positives))
    else:
        return (None, None)

