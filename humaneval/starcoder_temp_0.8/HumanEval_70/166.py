
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
    n = len(lst)
    sorted_list = []
    for i in range(n):
        if i % 2 == 0:
            min_index = lst.index(min(lst))
            sorted_list.append(lst.pop(min_index))
        else:
            max_index = lst.index(max(lst))
            sorted_list.append(lst.pop(max_index))
    return sorted_list
