
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
    arr = []
    for item in lst:
        if item not in arr:
            arr.append(item)

    for i in range(len(arr)):
        if arr[i] not in arr:
            arr.insert(i, arr[i])

    print(arr)
    return arr

