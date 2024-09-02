
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

    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return lst

    # make a new list of only the min and max values, then sort them
    new_lst = [min(lst), max(lst)]
    new_lst.sort()

    # calculate the midpoint
    mid = len(new_lst) // 2
    mid_val = new_lst[mid]

    # use the midpoint to calculate the index of the value in the original list
    mid_index = lst.index(mid_val)

    # remove the midpoint from new_lst
    new_lst.remove(mid_val)

    # generate a list of the same length as lst and return it
    out_lst = [lst[mid_index]]
    for i in range(len(lst) - 1):
        if i < mid_index:
            out_lst.append(new_lst[0])
            new_lst.remove(new_lst[0])
        elif i >= mid_index:
            out_lst.append(new_lst[-1])
            new_lst.remove(new_lst[-1])

    return out_lst

