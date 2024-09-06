
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

    lst_negative = [num for num in lst if num < 0]
    lst_positive = [num for num in lst if num > 0]

    if len(lst_negative) == 0:
        return None, None

    if len(lst_positive) == 0:
        return lst_negative[0], None

    return max(lst_negative), min(lst_positive)
