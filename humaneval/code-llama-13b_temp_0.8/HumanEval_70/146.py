
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
    max_index = 0
    new_list = []
    count = 0

    while len(lst) > count:
        min_index = lst.index(min(lst))
        max_index = lst.index(max(lst))
        if count % 2 == 0:
            new_list.append(lst[min_index])
            lst.pop(min_index)
        else:
            new_list.append(lst[max_index])
            lst.pop(max_index)
        count += 1
    return new_list

