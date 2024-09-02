
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
    negative_lst = [i for i in lst if i < 0]
    positive_lst = [i for i in lst if i > 0]
    if len(negative_lst) == 0 and len(positive_lst) == 0:
        return (None, None)
    elif len(negative_lst) > 0 and len(positive_lst) == 0:
        return (max(negative_lst), None)
    elif len(negative_lst) == 0 and len(positive_lst) > 0:
        return (None, max(positive_lst))
    elif len(negative_lst) > 0 and len(positive_lst) > 0:
        max_negative = max(negative_lst)
        max_positive = max(positive_lst)
        return (max_negative, max_positive)
