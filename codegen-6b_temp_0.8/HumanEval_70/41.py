
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
    length = len(lst)
    if length == 0:
        return []
    if length == 1:
        return lst
    if length == 2:
        return lst if lst[0] <= lst[1] else lst[::-1]
    new_lst = []
    lst.sort()
    max_val = lst[0]
    min_val = lst[-1]
    for i in range(length):
        val = lst[i]
        if val == max_val:
            new_lst.append(val)
            new_lst.append(min_val)
        if val == min_val:
            new_lst.append(val)
            new_lst.append(max_val)
        if val > max_val:
            new_lst.append(val)
            max_val = val
        if val < min_val:
            new_lst.append(val)
            min_val = val
    return new_lst

