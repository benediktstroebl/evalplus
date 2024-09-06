
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
    negative_lst = [x for x in lst if x < 0]
    positive_lst = [x for x in lst if x > 0]
    if not negative_lst and not positive_lst:
        return None, None
    largest_negative = max(negative_lst) if negative_lst else None
    smallest_positive = min(positive_lst) if positive_lst else None
    return largest_negative, smallest_positive

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
