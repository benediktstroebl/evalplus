
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
    if not lst:
        return None, None
    if any(x < 0 for x in lst):
        negatives = [x for x in lst if x < 0]
        if len(negatives) > 0:
            return max(negatives), min(lst)
        return None, None
    if any(x > 0 for x in lst):
        positives = [x for x in lst if x > 0]
        if len(positives) > 0:
            return min(positives), max(lst)
        return None, None
    return lst[0], lst[-1]