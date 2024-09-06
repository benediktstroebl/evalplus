
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

    # return the largest negative integer and smallest positive integer

    # sort the list first so that we can get negative numbers at the end and positive at the beginning
    lst = sorted(lst)

    # if there are no negative numbers, return None, None
    if lst[0] < 0:
        largest_negative = None
        smallest_positive = None
    else:
        largest_negative = lst[-1]
        smallest_positive = lst[0]

    # return the tuple
    return largest_negative, smallest_positive
