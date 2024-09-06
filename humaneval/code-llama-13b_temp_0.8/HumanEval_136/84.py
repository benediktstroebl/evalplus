
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
    if lst == []:
        return (None, None)
    
    max_small = 0
    min_big = 0

    for el in lst:
        if type(el) is int:
            if el < 0 and el > max_small:
                max_small = el
            if el >= 0 and el > min_big:
                min_big = el

    if max_small == 0:
        max_small = None
    if min_big == 0:
        min_big = None
    return (max_small, min_big)

