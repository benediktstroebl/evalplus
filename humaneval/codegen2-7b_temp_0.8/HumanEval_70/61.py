
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
    sorted_list = []
    for i in range(len(lst)):
        min_value = min(lst[:i+1])
        max_value = max(lst[i+1:])
        for j in range(min_value, max_value+1):
            sorted_list.append(j)
    return sorted_list
