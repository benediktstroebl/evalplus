
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
    lst1 = []
    lst2 = []

    for num in lst:
        if num < 0:
            lst1.append(num)
        elif num > 0:
            lst2.append(num)

    if len(lst1) == 0 and len(lst2) == 0:
        return (None, None)
    elif len(lst1) == 0:
        return (lst2[0], None)
    elif len(lst1) == 0:
        return (None, lst1[0])
    else:
        return (max(lst1), min(lst2))
