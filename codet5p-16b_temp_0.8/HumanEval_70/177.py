
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

    min_index = 0
    for i in range(len(lst)):
        if lst[i] < lst[min_index]:
            min_index = i
    for i in range(len(lst)):
        if lst[i] > lst[min_index]:
            lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

