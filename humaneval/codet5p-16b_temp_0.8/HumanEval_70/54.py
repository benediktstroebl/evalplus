
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

    sorted_list = sorted(lst)
    new_list = []
    min_value = min(lst)
    min_index = lst.index(min_value)
    for i in range(min_index):
        new_list.append(sorted_list[i])
    max_value = max(lst)
    max_index = lst.index(max_value)
    for i in range(max_index, len(lst)):
        new_list.append(sorted_list[i])
    return new_list

