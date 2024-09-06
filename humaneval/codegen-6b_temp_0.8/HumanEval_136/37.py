
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
    negative = [x for x in lst if x < 0]
    positive = [x for x in lst if x > 0]

    if not negative and not positive:
        return (None, None)

    if not negative:
        return (None, min(positive))

    if not positive:
        return (max(negative), None)

    return (max(negative), min(positive))

