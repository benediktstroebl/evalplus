
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
    sorted_lst = sorted(lst)
    if sorted_lst[0] > 0:
        b = sorted_lst[0]
    else:
        b = None
    if sorted_lst[-1] < 0:
        a = sorted_lst[-1]
    else:
        a = None
    return a, b


