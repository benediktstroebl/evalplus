
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
    neg = []
    pos = []
    for num in lst:
        if num < 0:
            neg.append(num)
        elif num > 0:
            pos.append(num)
    if neg == []:
        a = None
    else:
        a = max(neg)
    if pos == []:
        b = None
    else:
        b = min(pos)
    return (a, b)
