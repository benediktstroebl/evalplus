
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
    if lst == []:
        return []
    min = lst[0]
    max = lst[0]
    s_list = []
    for i in lst:
        if i < min:
            min = i
        if i > max:
            max = i
    for i in lst:
        if i < min:
            s_list.append(max)
            max = min
            min = i
        elif i > max:
            s_list.append(min)
            max = i
        else:
            s_list.append(i)
    return s_list
