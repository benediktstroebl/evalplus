
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
    lst = lst[:]
    lst.sort()
    result = []
    minimum = lst[0]
    index_min = 0
    for i in range(len(lst)):
        if lst[i] < minimum:
            minimum = lst[i]
            index_min = i
    result.append(minimum)
    for i in range(index_min):
        result.append(lst[i])
    for i in range(index_min+1, len(lst)):
        result.append(lst[i])
    return result

