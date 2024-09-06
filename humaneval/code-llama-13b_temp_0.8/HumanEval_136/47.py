
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

    # first find negative numbers
    neg = []
    pos = []
    for num in lst:
        if num < 0:
            neg.append(num)
        else:
            pos.append(num)
    # if no negative numbers, return None as a and find the smallest positive number as b
    if not neg:
        return (None, min(pos)) if pos else (None, None)
    # if no positive numbers, return None as b and find the largest negative number as a
    if not pos:
        return (max(neg), None)
    # if negative and positive numbers, return largest negative number as a and smallest positive number as b
    return max(neg), min(pos)
