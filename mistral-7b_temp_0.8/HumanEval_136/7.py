
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
    if not lst:
        return (None, None)
    if len(lst) == 1 and lst[0] == 0:
        return (None, None)

    a = None
    b = None

    for num in lst:
        if num > 0:
            if not b or num < b:
                b = num

        if num < 0:
            if not a or num > a:
                a = num
    return (a, b)



