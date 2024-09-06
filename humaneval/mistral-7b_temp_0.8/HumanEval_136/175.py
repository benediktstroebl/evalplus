
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
    # your code here
    lst_neg = [x for x in lst if x < 0]
    lst_pos = [x for x in lst if x > 0]

    if len(lst_pos) > 0:
        smallest_pos = min(lst_pos)
    else:
        smallest_pos = None

    if len(lst_neg) > 0:
        largest_neg = max(lst_neg)
    else:
        largest_neg = None

    return largest_neg, smallest_pos
