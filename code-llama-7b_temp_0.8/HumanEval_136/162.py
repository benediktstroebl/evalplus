
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
    pos = []
    neg = []
    # Use 'for' loop to check if the number is negative or positive.
    for i in lst:
        if i < 0:
            neg.append(i)
        elif i > 0:
            pos.append(i)
    # Check if the list is empty or not,
    # and return the right result.
    if len(neg) == 0 and len(pos) == 0:
        return (None, None)
    elif len(neg) == 0:
        return (None, min(pos))
    elif len(pos) == 0:
        return (max(neg), None)
    else:
        return (max(neg), min(pos))
