
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
    negative = [i for i in lst if i < 0]
    positive = [i for i in lst if i > 0]
    if not negative and not positive:
        return (None, None)
    elif not negative:
        return (max(positive), min(positive))
    elif not positive:
        return (max(negative), min(negative))
    return (max(negative), min(positive))
