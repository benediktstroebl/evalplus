
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
    positive = []
    negative = []
    for elem in lst:
        if elem > 0:
            positive.append(elem)
        elif elem < 0:
            negative.append(elem)
    if len(negative) == 0:
        return (None, None)
    elif len(negative) == 1 and negative[0] == 0:
        return (None, None)
    elif len(negative) == 1:
        return (negative[0], positive[0])
    else:
        return (negative[0], positive[0])
