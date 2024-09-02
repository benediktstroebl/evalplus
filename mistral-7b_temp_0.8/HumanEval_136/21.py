
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
    # Write code here
    if lst == []:
        return None, None

    lst_neg = []
    lst_pos = []
    for num in lst:
        if num < 0:
            lst_neg.append(num)
        else:
            lst_pos.append(num)

    if len(lst_neg) == 0 and len(lst_pos) == 0:
        return None, None

    elif len(lst_neg) == 0:
        return None, max(lst_pos)

    elif len(lst_pos) == 0:
        return min(lst_neg), None

    else:
        return min(lst_neg), max(lst_pos)


