
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
    negative_integers, positive_integers = [], []
    for i in lst:
        if i < 0:
            negative_integers.append(i)
        elif i > 0:
            positive_integers.append(i)
    if len(negative_integers) == 0:
        smallest_negative = None
    else:
        smallest_negative = min(negative_integers)
    if len(positive_integers) == 0:
        largest_positive = None
    else:
        largest_positive = max(positive_integers)
    return (smallest_negative, largest_positive)

