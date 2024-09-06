
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
    largest_smallest = (None, None)

    for n in lst:
        if n > 0:
            if n > largest_smallest[0]:
                largest_smallest = (n, largest_smallest[0])
        else:
            if n < largest_smallest[1]:
                largest_smallest = (largest_smallest[0], n)
    return largest_small
