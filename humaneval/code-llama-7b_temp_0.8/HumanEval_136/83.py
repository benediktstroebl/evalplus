
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

    largest_negative, smallest_positive = None, None

    for element in lst:
        if isinstance(element, int):
            if element < 0:
                largest_negative = element if largest_negative is None else max(element, largest_negative)
            elif element > 0:
                smallest_positive = element if smallest_positive is None else min(element, smallest_positive)

    return largest_negative, smallest_positive

