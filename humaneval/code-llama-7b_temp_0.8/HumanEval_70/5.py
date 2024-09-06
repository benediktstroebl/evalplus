
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
    if lst == []:
        return []
    else:
        minimum = min(lst)
        lst.remove(minimum)
        maximum = max(lst)
        lst.remove(maximum)
        result = [minimum]
        result.append(maximum)
        if lst == []:
            return result
        else:
            result.extend(strange_sort_list(lst))
            return result

