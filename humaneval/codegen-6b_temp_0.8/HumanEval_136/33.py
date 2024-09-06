
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
    lst = list(map(int, lst))
    lst_negative = [x for x in lst if x < 0] # return all elements from lst that are less than 0
    lst_positive = [x for x in lst if x > 0] # return all elements from lst that are greater than 0

    if lst_positive:
        a = max(lst_positive)
    else:
        a = None

    if lst_negative:
        b = min(lst_negative)
    else:
        b = None

    return (a, b)
