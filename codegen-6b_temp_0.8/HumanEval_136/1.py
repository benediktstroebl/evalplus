
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
    negative = lst[0]
    for num in lst:
        if num < 0:
            negative = num
        elif num > negative:
            negative = num
    positive = lst[0]
    for num in lst:
        if num > 0:
            positive = num
        elif num < positive:
            positive = num
    if negative is None:
        negative = None
    if positive is None:
        positive = None

    return (negative, positive)
