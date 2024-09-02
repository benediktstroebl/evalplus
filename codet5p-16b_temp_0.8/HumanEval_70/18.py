
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

    min_val = lst[0]
    max_val = lst[0]
    new_lst = []
    for i in range(1, len(lst)):
        if lst[i] <= min_val:
            min_val = lst[i]
        elif lst[i] >= max_val:
            max_val = lst[i]
    for j in range(len(lst)):
        if lst[j] == min_val:
            new_lst.append(max_val)
            max_val = min_val
            min_val = new_lst[-1]
    return new_lst



