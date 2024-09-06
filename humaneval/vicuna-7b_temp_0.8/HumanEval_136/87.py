
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
    positive = [x for x in lst if x > 0]
    negative = [x for x in lst if x < 0]
    if positive:
        if len(positive) > 0:
            return max(positive), min(positive)
    if negative:
        if len(negative) > 0:
            return min(negative), max(negative)
    return None, None