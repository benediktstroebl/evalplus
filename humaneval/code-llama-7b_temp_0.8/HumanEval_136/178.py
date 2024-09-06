
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
    # my_tuple = tuple()
    # if lst == []:
    #     return my_tuple
    # elif len(lst) == 1:
    #     if lst[0] >= 0:
    #         return (None, lst[0])
    #     else:
    #         return (lst[0], None)
    # else:
    #     negative_list = []
    #     positive_list = []
    #     for num in lst:
    #         if num < 0:
    #             negative_list.append(num)
    #         elif num > 0:
    #             positive_list.append(num)
    #     if len(negative_list) > 0:
    #         neg_max = max(negative_list)
    #     else:
    #         neg_max = None
    #     if len(positive_list) > 0:
    #         pos_min = min(positive_list)
    #     else:
    #         pos_min = None
    #     return (neg_max, pos_min)

    my_tuple = tuple()
    if lst == []:
        return my_tuple
    elif len(lst) == 1:
        if lst[0] >= 0:
            return (None, lst[0])
        else:
            return (lst[0], None)
    else:
        negative_list = []
        positive_list = []
        for num in lst:
            if num < 0:
                negative_list.append(num)
            elif num > 0:
                positive_list.append(num)
        if len(negative_list) > 0:
            neg_max = max(negative_list)
        else:
            neg_max = None
        if len(positive_list) > 0:
            pos_min = min(positive_list)
        else:
            pos_min = None
        return (neg_max, pos_min)

