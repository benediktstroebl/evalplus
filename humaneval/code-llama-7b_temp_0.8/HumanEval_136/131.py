
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
    for number in lst:
        if number < 0:
            negative_integers.append(number)
        elif number > 0:
            positive_integers.append(number)
    if negative_integers:
        neg = min(negative_integers)
    else:
        neg = None
    if positive_integers:
        pos = max(positive_integers)
    else:
        pos = None
    return neg, pos
