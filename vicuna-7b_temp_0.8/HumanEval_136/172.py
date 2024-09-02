
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
    max_lst = [-lst[0]]
    min_lst = [lst[-1]]
    for x in lst[1:]:
        if x < 0:
            max_lst.append(max(x, max_lst[-1]))
        else:
            min_lst.append(min(x, min_lst[-1]))
    return max_lst[0], min_lst[0]
