
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
    if not lst:
        return []

    n = len(lst)
    lst_reversed = lst[::-1]  # Reverse the list
    if n == 1:
        return lst_reversed[0]
    pivot = lst[0]
    for i in range(1, n):
        if lst[i] >= pivot:
            lst_reversed.insert(i, lst_reversed.pop(i))
        else:
            lst_reversed.insert(i, lst_reversed.pop(i-1))
    return lst_reversed
