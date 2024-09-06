
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
    max_int = None
    min_int = None

    for num in lst:
        if num >= 0 and (not min_int):
            min_int = num
        elif num < 0 and (not max_int):
            max_int = num
        elif max_int and num < 0 and num > max_int:
            max_int = num
        elif min_int and num >= 0 and num < min_int:
            min_int = num

    return (max_int, min_int)
