
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
    neg_nums = []
    pos_nums = []
    for i in lst:
        if i < 0:
            neg_nums.append(i)
        elif i > 0:
            pos_nums.append(i)
        else:
            continue

    if neg_nums == []:
        neg_num = None
    else:
        neg_num = max(neg_nums)

    if pos_nums == []:
        pos_num = None
    else:
        pos_num = min(pos_nums)

    return (neg_num, pos_num)
