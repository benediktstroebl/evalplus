
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
    result = [min(lst)]
    for i in lst:
        lst.pop(lst.index(i))
        if lst == []:
            result.append(i)
            break
        if max(lst) in lst:
            result.append(i)
            result.append(max(lst))
            lst.remove(max(lst))
        else:
            result.append(max(lst))
            lst.remove(max(lst))
            result.append(i)
    return result
    
