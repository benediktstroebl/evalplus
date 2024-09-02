
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
    result = []
    for item in lst:
        if lst.index(min(lst)) == 0:
            result.append(item)
        elif lst.index(max(lst)) == 0:
            result.append(min(lst))
            result.append(item)
            result.append(max(lst))
        else:
            result.append(item)
    return result

lst = [1, 2, 3, 4, 5, 5, 5, 5]
