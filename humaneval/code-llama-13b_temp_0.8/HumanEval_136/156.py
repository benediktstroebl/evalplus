
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
    small_positive = large_negative = None

    for num in lst:
        if num == 0:
            continue
        if num < 0:
            if large_negative is None or large_negative < num:
                large_negative = num
        else:
            if small_positive is None or small_positive > num:
                small_positive = num
    return (large_negative, small_positive)
