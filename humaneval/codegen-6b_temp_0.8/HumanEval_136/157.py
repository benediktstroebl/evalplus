
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
    max_negative, min_positive = None, None
    for num in lst:
        if num < 0:
            if max_negative is None or num > max_negative:
                max_negative = num
        else:
            if min_positive is None or num < min_positive:
                min_positive = num
    return (max_negative, min_positive)

