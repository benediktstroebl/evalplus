
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
    a = None
    b = None
    neg = 0
    pos = 0
    for item in lst:
        if item < 0:
            neg += 1
            if a == None:
                a = item
            elif item > a:
                a = item
        elif item > 0:
            pos += 1
            if b == None:
                b = item
            elif item < b:
                b = item

    if neg > 0 or pos > 0:
        return (a, b)
    else:
        return (None, None)

