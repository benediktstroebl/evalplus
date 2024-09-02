
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
    a = None
    b = None

    for i in lst:
        if i < 0:
            if a == None or i > a:
                a = i
        else:
            if b == None or i < b:
                b = i

    return (a, b)


assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
assert largest_smallest_integers([]) == (None, None)
assert largest_smallest_integers([0]) == (None, None)
assert largest_smallest_integers([-2, -1, -5, -4]) == (-2, -1)
assert largest_smallest_integers([7, 3, 100, -1, 12, -5, 10]) == (100, -1)