
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
    negative_lst = []
    positive_lst = []
    for num in lst:
        if num < 0:
            negative_lst.append(num)
        else:
            positive_lst.append(num)
    if len(negative_lst) == 0:
        return None, None
    else:
        return sorted(negative_lst)[-1], sorted(positive_lst)[0]



