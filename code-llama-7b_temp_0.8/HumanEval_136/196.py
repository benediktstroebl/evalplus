
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
    new_lst = []
    for i in lst:
        if type(i) == int:
            new_lst.append(i)
        else:
            continue
    if len(new_lst) == 0:
        return (None, None)
    else:
        return (max(i for i in new_lst if i < 0), min(i for i in new_lst if i > 0))

