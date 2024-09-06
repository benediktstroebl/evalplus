
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
    else:
        n = len(lst)
        i = j = 0
        while j < n-1:
            if lst[j] < lst[j+1]:
                i += 1
                lst.insert(j+1, lst.pop(i))
            j += 1
        return lst[:i]
