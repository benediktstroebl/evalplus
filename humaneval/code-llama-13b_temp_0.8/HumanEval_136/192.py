
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
    result_list = []
    for i in lst:
        if type(i) == int:
            result_list.append(i)
        else:
            pass
    result_list.sort()
    if result_list == []:
        return (None, None)
    else:
        return (result_list[0], result_list[-1])

