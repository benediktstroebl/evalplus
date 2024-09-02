
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
    # Please, insert your code here.
    # You can remove temporary variables, if it is needed.
    a = None
    b = None
    max_int = 0
    min_int = 0
    for i in lst:
        if i > max_int:
            max_int = i
        if i < min_int and i > 0:
            min_int = i
    a = max_int if max_int > 0 else None
    b = min_int if min_int < 0 else None
    return a, b

