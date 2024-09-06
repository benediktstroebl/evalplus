
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
    positive_lst = []
    negative_lst = []
    for num in lst:
        if num >= 0:
            positive_lst.append(num)
        else:
            negative_lst.append(num)
    if negative_lst:
        a = max(negative_lst)
    else:
        a = None
    if positive_lst:
        b = min(positive_lst)
    else:
        b = None
    return a, b
