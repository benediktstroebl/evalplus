
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
    else:
        result = []
        low = min(lst)
        high = max(lst)
        while lst:
            result.append(low)
            lst.remove(low)
            low = high
            if lst:
                high = max(lst)
                lst.remove(high)
                result.append(high)
                lst.remove(low)
        return result
