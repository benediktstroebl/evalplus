
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
    all_negative = all(x < 0 for x in lst)
    all_positive = all(x > 0 for x in lst)
    if all_negative or all_positive:
        return (None, None)
    return (max(x for x in lst if x < 0), min(x for x in lst if x > 0))

