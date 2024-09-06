
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
    negative_integer = None
    positive_integer = None
    for i in lst:
        if i < 0:
            negative_integer = i
            if positive_integer!= None:
                break
        elif i > 0:
            positive_integer = i
            if negative_integer!= None:
                break
    return (negative_integer, positive_integer)
