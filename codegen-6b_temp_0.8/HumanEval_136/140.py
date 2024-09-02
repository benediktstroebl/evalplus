
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
        return (None, None)
    new_list = sorted(lst)
    neg_list = [x for x in new_list if x < 0]
    pos_list = [x for x in new_list if x > 0]
    if len(neg_list) == 0:
        neg = None
    else:
        neg = neg_list[-1]
    if len(pos_list) == 0:
        pos = None
    else:
        pos = pos_list[0]
    return (neg, pos)

import unittest
