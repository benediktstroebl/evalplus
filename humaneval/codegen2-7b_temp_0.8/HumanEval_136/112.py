
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
    n_neg = 0
    n_pos = 0
    largest = 0
    smallest = 0
    for num in lst:
        if num < 0:
            n_neg += 1
            largest = max(largest, num)
        else:
            n_pos += 1
            smallest = min(smallest, num)
    if n_neg == n_pos:
        return (None, None)
    else:
        return (largest, smallest
