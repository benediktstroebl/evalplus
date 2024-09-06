
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
    lst_sorted = sorted(lst)
    result = []
    n = len(lst)

    while n != 0:
        min_val = lst_sorted[0]
        for i in range(len(lst)):
            if lst[i] == min_val:
                break
        lst.remove(min_val)
        lst_sorted.remove(min_val)
        result.append(min_val)
        n -= 1

    return result
