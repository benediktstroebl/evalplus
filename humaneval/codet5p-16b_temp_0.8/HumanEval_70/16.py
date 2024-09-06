
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

    minimum = lst[0]
    maximum = lst[0]

    for i in range(1, len(lst)):
        if lst[i] < minimum:
            minimum = lst[i]
        elif lst[i] > maximum:
            maximum = lst[i]

    sorted_list = []

    for _ in range(len(lst)):
        sorted_list.append(minimum)
        lst.remove(minimum)
        if len(lst) == 0:
            break
        maximum = lst[0]
        for i in range(1, len(lst)):
            if lst[i] > maximum:
                maximum = lst[i]
        minimum = maximum

    return sorted_list

