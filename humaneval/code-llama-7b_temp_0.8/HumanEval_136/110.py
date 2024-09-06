
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
    # Your code here
    result = []
    for x in lst:
        if x < 0:
            result.append(x)

    result.sort()
    neg = result[-1]

    result2 = []
    for y in lst:
        if y > 0:
            result2.append(y)

    result2.sort()
    pos = result2[0]

    if neg is None and pos is None:
        return (None, None)
    else:
        return (neg, pos)
