
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
    try:
        lst_neg = filter(lambda num: num < 0, lst)
        largest_neg = max(lst_neg)
        lst_pos = filter(lambda num: num >= 0, lst)
        smallest_pos = min(lst_pos)
        return (largest_neg, smallest_pos)
    except:
        return (None, None
