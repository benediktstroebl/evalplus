
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

    if lst == []:
        return (None, None)
    elif lst == [0]:
        return (None, None)
    else:
        max, min = None, None
        for x in lst:
            if x > 0:
                if not max:
                    max = x
                else:
                    max = max if max > x else x
            if x < 0:
                if not min:
                    min = x
                else:
                    min = min if min < x else x
        return (max, min)
    











