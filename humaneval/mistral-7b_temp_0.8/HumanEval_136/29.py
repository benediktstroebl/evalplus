
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
    # your code here
    max_negative_int, min_positive_int = None, None
    for n in lst:
        if n > 0:
            if min_positive_int is None or n < min_positive_int:
                min_positive_int = n
        elif n < 0:
            if max_negative_int is None or n > max_negative_int:
                max_negative_int = n
    return (max_negative_int, min_positive_int)

