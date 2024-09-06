
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

    if not any(isinstance(n, int) for n in lst):
        return (None, None)

    if not any(isinstance(n, int) and n < 0 for n in lst):
        smallest_positive = None
    else:
        smallest_positive = min(n for n in lst if isinstance(n, int) and n > 0)

    if not any(isinstance(n, int) and n > 0 for n in lst):
        largest_negative = None
    else:
        largest_negative = max(n for n in lst if isinstance(n, int) and n < 0)

    return (largest_negative, smallest_positive)

