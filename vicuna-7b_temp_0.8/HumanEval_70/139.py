
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
    lst = lst[::-1]
    max_index = 0
    min_value = max(lst)
    for i in range(1, len(lst)):
        if lst[i] == max_value:
            max_index += 1
            max_value = lst[i]
        else:
            min_value = max(lst[i])
            min_index = i
    return [lst[i*-1] for i in range(max_index+1)]
