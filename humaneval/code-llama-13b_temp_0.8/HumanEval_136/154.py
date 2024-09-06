
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
    # lst = list(lst)
    # lst_set = set(lst)
    # if len(lst_set) == 1 and lst[0] == 0:
    #     return (None, None)
    # elif len(lst_set) == 1:
    #     return (None, lst[0])
    # lst.sort()
    # smallest = lst.index(min(lst))
    # largest = lst.index(max(lst))
    # return (lst[largest], lst[smallest])

    # the same as above, but even shorter
    lst_set = set(lst)
    if len(lst_set) == 1:
        return (None, None)
    elif len(lst_set) == 2:
        if lst[0] > 0:
            return (None, lst[1])
        elif lst[1] > 0:
            return (None, lst[0])
        else:
            return (lst[1], lst[0])
    else:
        largest = min(filter(lambda x: x > 0, lst))
        smallest = max(filter(lambda x: x < 0, lst))
        return (largest, smallest)

