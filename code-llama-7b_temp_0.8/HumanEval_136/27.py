
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
    negative_integers = []
    positive_integers = []

    for item in lst:
        if item < 0:
            negative_integers.append(item)
        elif item > 0:
            positive_integers.append(item)

    if len(negative_integers) > 0:
        a = max(negative_integers)
    else:
        a = None

    if len(positive_integers) > 0:
        b = min(positive_integers)
    else:
        b = None

    return (a, b)

