
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
    negative_integers = []
    positive_integers = []
    for integer in lst:
        if integer < 0:
            negative_integers.append(integer)
        elif integer > 0:
            positive_integers.append(integer)
    if not negative_integers:
        return (None, None)
    if not positive_integers:
        return (None, None)
    largest = negative_integers[0]
    for integer in positive_integers:
        if integer > largest:
            largest = integer
    return (largest, positive_integers[0])



