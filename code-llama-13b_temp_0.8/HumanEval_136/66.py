
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
    positive_integers = [el for el in lst if el > 0]
    negative_integers = [el for el in lst if el < 0]
    if len(positive_integers) == 0:
        smallest_integer = None
    else:
        smallest_integer = sorted(positive_integers)[0]
    if len(negative_integers) == 0:
        largest_integer = None
    else:
        largest_integer = sorted(negative_integers)[-1]
    return (largest_integer, smallest_integer)

