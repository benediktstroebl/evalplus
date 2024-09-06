
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

    new_lst = []
    for i in range(len(lst)):
        min_val = lst[i]
        max_val = lst[i]
        for j in range(i+1, len(lst)):
            if lst[j] < min_val:
                min_val = lst[j]
            if lst[j] > max_val:
                max_val = lst[j]
        new_lst.append(min_val)
        new_lst.append(max_val)

    return new_lst

