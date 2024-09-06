
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
        return (None, None)
    if len(lst) == 1:
        if lst[0] > 0:
            return (None, lst[0])
        else:
            return (lst[0], None)
    if len(lst) == 2:
        if lst[0] < 0 and lst[1] > 0:
            return (None, min(lst))
        elif lst[0] > 0 and lst[1] < 0:
            return (max(lst), None)
        elif lst[0] < 0 and lst[1] < 0:
            return (max(lst), min(lst))
        else:
            return (None, None)
    if len(lst) > 2:
        negative = []
        positive = []
        for num in lst:
            if num < 0:
                negative.append(num)
            elif num > 0:
                positive.append(num)
        if len(negative) == 0 and len(positive) > 0:
            return (max(positive), None)
        elif len(positive) == 0 and len(negative) > 0:
            return (None, min(negative))
        elif len(negative) == 0 and len(positive) == 0:
            return (None, None)
        else:
            return (max(negative), min(positive))

