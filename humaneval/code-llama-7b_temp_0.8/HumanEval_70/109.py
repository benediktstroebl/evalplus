
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
    new_list = lst.copy()
    new_list.sort()
    result = []

    while len(new_list) > 0:
        minimum = min(new_list)
        new_list.remove(minimum)
        result.append(minimum)
        if len(new_list) == 0:
            break
        maximum = max(new_list)
        new_list.remove(maximum)
        result.append(maximum)
    
    return result



