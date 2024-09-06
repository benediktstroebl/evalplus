
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
    # 1st iter determines min and max
    # 2nd iter swaps each item with the min
    # 3rd iter swaps each item with the max
    lst_copy = lst.copy()
    min, max = min(lst_copy), max(lst_copy)
    lst_copy.sort()
    i, j = 0, len(lst_copy) - 1
    while i < j:
        lst[i], lst[j] = min, max
        i += 1
        j -= 1
        min, max = min(lst_copy[i:]), max(lst_copy[i:])
        lst_copy.sort()
        i, j = 0, len(lst_copy) - 1
        while i < j:
            lst[i], lst[j] = min, max
            i += 1
            j -= 1
            min, max = min(lst_copy[i:]), max(lst_copy[i:])
            lst_copy.sort()

