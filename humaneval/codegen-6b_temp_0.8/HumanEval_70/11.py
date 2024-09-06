
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
    if len(lst) == 0:
        return []
    # First i elements are sorted
    lst1 = lst[:len(lst) // 2]
    # Then i elements are sorted
    lst2 = lst[len(lst) // 2:]
    lst1.sort()
    lst2.sort(reverse=True)
    return lst1 + lst2
