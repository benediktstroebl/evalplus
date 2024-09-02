
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
    lst = sorted(lst)
    return lst[-1], lst[0]


assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (1, 7)
assert largest_smallest_integers([]) == (None, None)
assert largest_smallest_integers([0]) == (None, None)
assert largest_smallest_integers([-2, 2, 4, 1, 3, 5, 7]) == (-2, -2)
assert largest_smallest_integers([-13, -14, -15, -16, -17, -18, -19, -20]) == (None, -20)
assert largest_smallest_integers([-13, -13, -14, -15, -16, -17, -18, -19, -20]) == (-13, -13)
assert largest_smallest_integers([-13, -13, -14, -14, -15, -16, -17, -18, -19, -20]) == (-14, -14)
assert largest_smallest_integers([-13, -13, -14, -14, -15, -16, -17, -18, -19, -21]) == (-14, -14)
assert largest_smallest_integers([-13, -13, -14, -14, -15, -16, -17, -18, -19, -21, -20]) == (-14, -14)
assert largest_smallest_integers([-13, -13, -14, -14, -15, -16, -17, -18, -19, -20, -21]) == (-14, -14)
