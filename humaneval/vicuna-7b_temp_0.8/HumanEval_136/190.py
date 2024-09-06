
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
    def count_neg(lst):
        neg_cnt = 0
        for x in lst:
            if x < 0:
                neg_cnt += 1
        return neg_cnt

    def count_pos(lst):
        pos_cnt = 0
        for x in lst:
            if x > 0:
                pos_cnt += 1
        return pos_cnt

    count_neg_lst = count_neg(lst)
    count_pos_lst = count_pos(lst)

    if count_neg_lst > 0 and count_pos_lst == 0:
        return (0, None)

    if count_neg_lst == 0 and count_pos_lst > 0:
        return (None, 0)

    if count_neg_lst == 0 and count_pos_lst == 0:
        return (None, None)

    if count_neg_lst > count_pos_lst:
        return (lst[0], None)

    if count_neg_lst < count_pos_lst:
        return (lst[0], lst[-1])

    return (lst[0], lst[-1])