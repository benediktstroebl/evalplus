
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
        return lst

    arr = lst.copy()
    res = [arr[0]]
    for i in range(len(arr)):
        if arr[i] == min(arr):
            res.append(arr[i])
            arr.remove(min(arr))
        else:
            res.append(max(arr))
            arr.remove(max(arr))

    return res

