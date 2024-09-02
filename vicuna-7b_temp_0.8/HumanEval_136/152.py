
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
    n = len(lst)
    if n == 0:
        return (None, None)
    if n == 1:
        return (lst[0], lst[0])

    negative_count = 0
    positive_count = 0

    for num in lst:
        if num < 0:
            negative_count += 1
        else:
            positive_count += 1

    if negative_count == 0 and positive_count == 0:
        return (None, None)

    max_neg = float('-inf')
    max_pos = float('inf')
    min_pos = float('inf')
    min_neg = float('-inf')

    for num in lst:
        if num < 0:
            max_neg = min(max_neg, num)
        elif num > 0:
            max_pos = min(max_pos, num)
        elif num > 0:
            min_pos = max(min_pos, num)
        elif num < 0:
            min_neg = max(min_neg, num)

    return (max_neg, min_pos)