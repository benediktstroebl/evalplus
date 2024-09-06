
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
    largest_neg, smallest_pos = None, None
    for i in lst:
        if type(i) is int:
            if i < 0:
                if largest_neg is None:
                    largest_neg = i
                else:
                    largest_neg = i if i > largest_neg else largest_neg
            elif i > 0:
                if smallest_pos is None:
                    smallest_pos = i
                else:
                    smallest_pos = i if i < smallest_pos else smallest_pos
    return (largest_neg, smallest_pos)

