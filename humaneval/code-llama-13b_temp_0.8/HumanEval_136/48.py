
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
    negative = []
    positive = []
    for el in lst:
        if type(el) is int:
            if el < 0:
                negative.append(el)
            elif el > 0:
                positive.append(el)

    if len(negative) == 0:
        negative = None
    else:
        negative = max(negative)

    if len(positive) == 0:
        positive = None
    else:
        positive = min(positive)

    return negative, positive

