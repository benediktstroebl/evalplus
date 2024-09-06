
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
    # print("largest_smallest_integers: " + str(lst))
    if not lst:
        return None, None
    elif lst.count(0) > 1:
        return None, None
    elif lst.count(0) == 1:
        return None, None
    else:
        max_neg = max(filter(lambda x: x < 0, lst))
        min_pos = min(filter(lambda x: x > 0, lst))
        # print(str(max_neg) + ' ' + str(min_pos))
        return max_neg, min_pos

