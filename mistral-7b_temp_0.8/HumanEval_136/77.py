
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
    elif len(lst) == 1 and lst[0] > 0:
        return None, lst[0]
    elif len(lst) == 1 and lst[0] < 0:
        return lst[0], None
    else:
        neg = lst[0]
        pos = lst[0]
        for i in range(1, len(lst)):
            if lst[i] > 0:
                if pos == None:
                    pos = lst[i]
                elif pos < lst[i]:
                    pos = lst[i]
            elif lst[i] < 0:
                if neg == None:
                    neg = lst[i]
                elif neg > lst[i]:
                    neg = lst[i]
        return neg, pos
