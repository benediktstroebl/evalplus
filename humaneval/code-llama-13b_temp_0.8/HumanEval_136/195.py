
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
    if not lst or not any(isinstance(x, int) for x in lst):
        return (None, None)
    lst_filtered = list(filter(lambda x: isinstance(x, int), lst))
    if all(x >= 0 for x in lst_filtered):
        return (None, min(lst_filtered))
    elif all(x <= 0 for x in lst_filtered):
        return (max(lst_filtered), None)
    else:
        return (max(filter(lambda x: x < 0, lst_filtered)), min(filter(lambda x: x >= 0, lst_filtered)))

