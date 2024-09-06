
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
    if n == 0:
        return []
    else:
        first_val = lst[0]
        last_val = lst[n-1]
        for i in range(1, n):
            if lst[i] < first_val:
                first_val, last_val = lst[i], lst[i-1]
        return lst[0:n]
