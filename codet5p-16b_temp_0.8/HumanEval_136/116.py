
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

    if len(lst) == 0:
        return None, None
    elif len(lst) == 1:
        return None, lst[0]
    else:
        lst = sorted(lst)
        max = 0
        min = 0
        if lst[0] < 0:
            min = lst[0]
        else:
            max = lst[0]
        for i in range(1, len(lst)):
            if lst[i] > 0:
                min = lst[i]
                break
            else:
                if lst[i] < max:
                    max = lst[i]
        return max, min

