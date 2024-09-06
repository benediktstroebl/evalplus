
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
    n = len(lst)
    for i in range(n):
        min_index = 0
        min_val = lst[0]
        for j in range(1, n):
            if lst[j] < lst[min_index]:
                min_index = j
                min_val = lst[j]
        lst[i:i+1] = [min_val, lst[min_index]]
    return lst
