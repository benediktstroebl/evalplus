
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
    num1 = None
    num2 = None
    for i in lst:
        if i > num1 and i < 0:
            num1 = i
        elif i < num1 and i > 0:
            num2 = i
    if num1 is not None:
        return (num1, num2)
    else:
        return None
    pass
