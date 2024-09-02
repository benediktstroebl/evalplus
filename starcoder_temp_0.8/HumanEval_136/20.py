
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
    positives = [x for x in lst if x >= 0]
    negatives = [x for x in lst if x < 0]
    largest = None
    smallest = None
    if len(positives) == 0:
        largest = None
        smallest = None
    elif len(negatives) == 0:
        largest = positives[0]
        smallest = positives[0]
    else:
        smallest = min(negatives)
        largest = max(positives)
    return (largest, smallest)
