
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
    negative_int = []
    positive_int = []
    for integer in lst:
        if integer < 0:
            negative_int.append(integer)
        else:
            positive_int.append(integer)
    if len(negative_int) > 0:
        return (min(negative_int), max(positive_int))
    else:
        return (None, None)

