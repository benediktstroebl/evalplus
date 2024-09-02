
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
    lst_length = len(lst)

    if lst_length == 0:
        return None, None
    elif lst_length == 1:
        return lst[0], None
    else:
        smallest_positive = min(lst)
        smallest_negative = max(-lst)
        return smallest_positive, smallest_negative
