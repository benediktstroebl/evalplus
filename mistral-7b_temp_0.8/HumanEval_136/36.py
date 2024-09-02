
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
    lst = [int(x) for x in lst]
    if not lst:
        return None, None

    if len(lst) == 1:
        return lst[0], None

    max_neg_int = max(lst[i] for i in range(len(lst)) if lst[i] < 0)
    min_pos_int = min(lst[i] for i in range(len(lst)) if lst[i] > 0)
    return max_neg_int, min_pos_int


