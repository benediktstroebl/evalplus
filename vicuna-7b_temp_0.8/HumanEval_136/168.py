
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
    positive_lst = filter(lambda x: x > 0, lst)
    negative_lst = filter(lambda x: x < 0, lst)

    if len(positive_lst) > 0 and len(negative_lst) > 0:
        if len(positive_lst) > len(negative_lst):
            a = max(positive_lst)
            b = max(negative_lst)
        else:
            a = max(negative_lst)
            b = max(positive_lst)
    else:
        a = None
        b = None

    return a, b
