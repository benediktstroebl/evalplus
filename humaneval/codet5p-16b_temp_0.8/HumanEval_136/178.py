
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

    min_list = []
    max_list = []
    for i in lst:
        if i < 0:
            min_list.append(i)
        elif i > 0:
            max_list.append(i)
    if min_list == []:
        a = None
    else:
        a = max(min_list)
    if max_list == []:
        b = None
    else:
        b = min(max_list)
    return (a, b)
