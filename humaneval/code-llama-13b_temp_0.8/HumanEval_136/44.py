
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

    if len(lst) == 0:
        return (None, None)

    negative_integer = []
    positive_integer = []
    for integer in lst:
        if integer < 0:
            negative_integer.append(integer)
        elif integer > 0:
            positive_integer.append(integer)

    if not negative_integer and not positive_integer:
        return (None, None)

    if not negative_integer:
        return (None, min(positive_integer))

    if not positive_integer:
        return (max(negative_integer), None)

    return (max(negative_integer), min(positive_integer))

