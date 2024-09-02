
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
    # Tricky part, swap max and min
    if not lst:
        return []
    if lst[0] == lst[1]:
        return lst[0]
    return [lst[0]] + [lst[lst[0].index(lst[1]) + 1] for _ in range(lst[0]-1)] + [lst[lst[0].index(lst[1])]]
