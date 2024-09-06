
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
    if len(lst) == 0:
        return (None, None)
    if len(lst) == 1:
        if lst[0] < 0:
            return (lst[0], None)
        return (None, lst[0])
    min_ = float('inf')
    max_ = float('-inf')
    for item in lst:
        if isinstance(item, int) == True:
            if item < min_:
                min_ = item
            if item > max_:
                max_ = item
    if min_ == float('inf'):
        min_ = None
    if max_ == float('-inf'):
        max_ = None
    return (max_, min_)

