
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
    negative_int = None
    positive_int = None
    if len(lst) == 0:
        return None, None
    for i in lst:
        if i < 0:
            if negative_int == None:
                negative_int = i
            else:
                negative_int = negative_int if negative_int > i else i
        if i > 0:
            if positive_int == None:
                positive_int = i
            else:
                positive_int = positive_int if positive_int < i else i
    return (negative_int, positive_int)

