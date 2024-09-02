
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
    largest_negative_integer = None
    smallest_positive_integer = None
    largest_positive_integer = None
    smallest_negative_integer = None

    for integer in lst:
        if isinstance(integer, int):
            if integer > 0:
                if largest_positive_integer:
                    if integer > largest_positive_integer:
                        largest_positive_integer = integer
                else:
                    largest_positive_integer = integer
            else:
                if smallest_negative_integer:
                    if integer < smallest_negative_integer:
                        smallest_negative_integer = integer
                else:
                    smallest_negative_integer = integer

    if not smallest_positive_integer and not largest_negative_integer:
        return None, None

    return largest_negative_integer, smallest_positive_integer

