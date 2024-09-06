
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
    large = None
    small = None
    if lst:
        for i in lst:
            if i < 0:
                if large is None:
                    large = i
                else:
                    if large < i:
                        large = i
            if i > 0:
                if small is None:
                    small = i
                else:
                    if small > i:
                        small = i
    return (large, small)

