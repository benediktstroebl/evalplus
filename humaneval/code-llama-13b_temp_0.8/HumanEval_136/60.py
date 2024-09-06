
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
    # return (None, None) if len(lst) == 0
    # return (None, min(lst)) if all(i <= 0 for i in lst)
    # return (max(lst), None) if all(i >= 0 for i in lst)
    # return (None, min(lst)) if all(i <= 0 for i in lst)
    # return (max(lst), None) if all(i >= 0 for i in lst)

    # lst = [2, 4, 1, 3, 5, 7]

    # print('max:', max([i for i in lst if i > 0]))
    # print('min:', min([i for i in lst if i < 0]))
    # print(max([i for i in lst if i >= 0]))
    # print(min([i for i in lst if i <= 0]))

    # return (max(lst) if all(i >= 0 for i in lst) else None,
    #         min(lst) if all(i >= 0 for i in lst) else None)

    # if not lst:
    #     return (None, None)
    # if all(i >= 0 for i in lst):
    #     return (max(lst), min(lst))
    # if all(i <= 0 for i in lst):
    #     return (max(lst), min(lst))
    # return (None, None)

    # print(min([i for i in lst if i < 0]))
    # return (max([i for i in lst if i < 0]), min([i for i in lst if i < 0])) if lst else (None, None)
    # return (None, None) if len(lst) == 0 else (max([i for i in lst if i >= 0]), min([i for i in lst if i < 0]))
    # return (max([i for i in lst if i < 0]), min([i for i in lst if i < 0])) if lst else (None, None)
    return (max(lst) if all(i >= 0 for i in lst) else None,
            min
