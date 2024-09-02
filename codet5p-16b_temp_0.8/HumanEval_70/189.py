
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

    lst.sort()
    sorted_list = []
    min_value = lst[0]
    for i in range(len(lst)):
        if i % 2 == 0:
            sorted_list.append(lst[i])
        else:
            sorted_list.append(lst[i - 1])
    return sorted_list
