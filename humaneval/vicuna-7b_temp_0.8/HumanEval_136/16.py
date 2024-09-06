
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
    largest_idx = 0
    smallest_idx = len(lst) - 1
    for i in range(1, len(lst)):
        if lst[i] < 0:
            largest_idx = i
        elif lst[i] > 0:
            smallest_idx = i
    return lst[largest_idx], lst[smallest_idx]
