
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

    largest_neg = None
    smallest_pos = None

    for n in lst:
        if isinstance(n, int):
            if n > 0:
                if smallest_pos == None or n < smallest_pos:
                    smallest_pos = n
            else:
                if largest_neg == None or n > largest_neg:
                    largest_neg = n
    return largest_neg, smallest_pos

