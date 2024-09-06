
def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''

    # create new_list to return
    new_list = []
    # remove duplicates and sort list
    lst = list(set(lst))
    lst.sort()
    # create range of size of list
    lst_range = range(len(lst))

    # loop through lst_range
    for i in lst_range:
        # check if i is even
        if i % 2 == 0:
            # add minimum to new_list
            new_list.append(min(lst))
            # pop minimum from lst
            lst.pop(lst.index(min(lst)))
        # if i is odd
        else:
            # add maximum to new_list
            new_list.append(max(lst))
            # pop maximum from lst
            lst.pop(lst.index(max(lst)))

    # return new_list
    return new_list

