
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
    #first check if there is any negative or positive integers in the list
    neg_pos_flag = False
    for elem in lst:
        if elem > 0:
            neg_pos_flag = True
        elif elem < 0:
            neg_pos_flag = False
            break
    if neg_pos_flag == False:
        return None, None

    #if there is no negative or positive integers, return None
    max_neg = -100
    min_pos = 100
    for elem in lst:
        if elem > 0:
            min_pos = min(min_pos, elem)
        elif elem < 0:
            max_neg = max(max_neg, elem)
    if max_neg == -100 or min_pos == 100:
        return None, None
    else:
        return max_neg, min_pos

assert largest_smallest_integers([]) == (None, None)
assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
assert largest_smallest_integers([1, 2, 3, 4]) == (None, None)
assert largest_smallest_integers([-100, -1, -3, -5, -7]) == (-7, 100)
assert largest_smallest_integers([-5, -4, 1, 2, 3 ]) == (-5, 1)
assert largest_smallest_integers([-1, -2, -3]) == (None, None)
assert largest_smallest_integers([1, 2, 3]) == (None, None)
assert largest_smallest_integers([-1, 2, 3]) == (None, None)
assert largest_smallest_integers([-3, -1, -2, -4]) == (None, None)
assert largest_smallest_integers([-3, 2, -1, -2, -4]) == (-1, 2)
assert largest_smallest_integers([-3, 2, -1, 2, 4]) == (-3, 1)
assert largest_smallest_integers([-3, 2, -1,