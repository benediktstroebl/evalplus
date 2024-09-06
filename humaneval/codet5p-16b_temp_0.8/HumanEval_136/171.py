
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

    negative_integers = list(filter(lambda x: x < 0, lst))
    positive_integers = list(filter(lambda x: x > 0, lst))

    if negative_integers == [] and positive_integers == []:
        return (None, None)

    if negative_integers == []:
        return (None, min(positive_integers))

    if positive_integers == []:
        return (max(negative_integers), None)

    return (max(negative_integers), min(positive_integers))

