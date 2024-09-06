
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
    length = len(lst)
    if length == 0:
        return []

    result = [lst[0]]
    for i in range(length):
        if result[0] > lst[i]:
            result.insert(0, lst[i])
        else:
            result.append(lst[i])

    return result

