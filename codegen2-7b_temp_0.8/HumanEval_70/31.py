
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

    current_min = lst[0]
    current_max = lst[len(lst) - 1]

    for i in range(len(lst) - 1):
        if lst[i] > current_max:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            current_max = lst[i]
        elif lst[i] < current_min:
            lst[i], lst[i + 1] = lst[i + 1], lst[i
