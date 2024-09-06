
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
    # My solution
    def is_positive(x):
        if x > 0:
            return True
        else:
            return False

    def is_negative(x):
        if x < 0:
            return True
        else:
            return False

    pos_list = []
    neg_list = []

    for i in lst:
        if is_positive(i):
            pos_list.append(i)
        elif is_negative(i):
            neg_list.append(i)
        else:
            continue
    try:
        return (min(neg_list), max(pos_list))
    except:
        return (None, None)

    # Cleverer solution
    '''
    def is_positive(x):
        return (x > 0) - (x < 0)

    negatives = [x for x in lst if is_positive(x) < 0]
    positives = [x for x in lst if is_positive(x) > 0]

    return (min(negatives) if negatives else None, max(positives) if positives else None)
    '''
