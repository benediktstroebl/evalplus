
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

    min_index = 0
    max_index = 1

    for i in range(1, len(lst)):
        if lst[i] < lst[min_index]:
            min_index = i
        elif lst[i] > lst[max_index]:
            max_index = i

    strange_lst = lst[:min_index]
    strange_lst.append(lst[max_index])

    for i in range(1, len(lst) - 1):
        if lst[i] > lst[max_index]:
            if lst[i] < lst[min_index]:
                min_index = i
            strange_lst.append(lst[i])
            strange_lst.append(lst[max_index])
        elif lst[i] < lst[min_index]:
            strange_lst.append(lst[i])
            strange_lst.append(lst[min_index])

    strange_lst.append(lst[-1])

    return strange_lst
