
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
    lst = list(lst)
    temp_lst = []
    min_val = max(lst)
    for i in range(len(lst) - 1):
        if lst[i] >= min_val:
            min_val = lst[i]
        else:
            temp_lst.append(lst[i])
    return temp_lst + [min_val] + [lst[i] for i in range(len(lst)) if lst[i] < min_val]
