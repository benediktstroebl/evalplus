
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
    # 1. First create the negative list
    neg_lst = [item for item in lst if item < 0]
    # 2. If there are no negative integers, return None
    if not neg_lst:
        return None, None
    # 3. Find the largest negative integer
    negative_max = max(neg_lst)
    # 4. Create the positive list
    pos_lst = [item for item in lst if item > 0]
    # 5. If there are no positive integers, return None
    if not pos_lst:
        return None, None
    # 6. Find the smallest positive integer
    positive_min = min(pos_lst)
    return negative_max, positive_min
