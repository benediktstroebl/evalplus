
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
    largest_negative = None
    smallest_positive = None
    for item in lst:
        if type(item) is not int:
            continue
        if item < 0:
            if largest_negative == None or largest_negative < item:
                largest_negative = item
        if item > 0:
            if smallest_positive == None or smallest_positive > item:
                smallest_positive = item
    return (largest_negative, smallest_positive)

