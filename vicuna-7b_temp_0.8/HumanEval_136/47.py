
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
    max_lst = [max(lst) if x > 0 else x for x in lst]
    min_lst = [min(lst) if x > 0 else x for x in lst]
    if max_lst and min_lst:
        return max_lst[0], min_lst[0]
    else:
        return None, None

print(largest_smallest_integers([-3, -4, 0, 1, 2, 3, 4, 5, 7, 8, 9]))
