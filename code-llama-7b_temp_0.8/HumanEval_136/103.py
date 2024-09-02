
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
    pos_nums = []
    neg_nums = []
    for x in lst:
        if x < 0:
            neg_nums.append(x)
        else:
            pos_nums.append(x)
    if neg_nums != []:
        neg_nums.sort()
        neg_num = neg_nums[-1]
    else:
        neg_num = None
    if pos_nums != []:
        pos_nums.sort()
        pos_num = pos_nums[0]
    else:
        pos_num = None
    return (neg_num, pos_num)
