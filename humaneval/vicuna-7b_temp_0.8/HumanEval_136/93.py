
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
    largest_positives = [x for x in lst if x > 0]
    largest_negatives = [x for x in lst if x < 0]
    if largest_positives and largest_negatives:
        largest_positives.sort()
        largest_negatives.sort()
        return largest_positives[0], largest_negatives[-1]
    elif largest_positives or largest_negatives:
        return None, None
    else:
        return None, None

lst = [2, 4, 1, 3, 5, 7]
