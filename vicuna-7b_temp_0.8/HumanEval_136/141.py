
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
    if not lst:
        return (None, None)
    else:
        positive_lst = [i for i in lst if i > 0]
        negative_lst = [i for i in lst if i < 0]
        if positive_lst or negative_lst:
            a = max(positive_lst) if positive_lst else min(negative_lst)
            b = max(negative_lst) if negative_lst else min(positive_lst)
        else:
            a = None
            b = None
        return a, b
