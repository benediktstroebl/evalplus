
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
    arr_min_max = []
    for i in lst:
        if i <= lst[-1]:
            arr_min_max.append(i)
        else:
            arr_min_max.append(lst[-1])
            arr_min_max.append(i)
    
    for j in range(len(arr_min_max)):
        for k in range(j+1, len(arr_min_max)):
            if arr_min_max[j] > arr_min_max[k]:
                arr_min_max[j], arr_min_max[k] = arr_min_max[k], arr_min_max[j]
    
    for i in range(len(arr_min_max)):
        arr.append(arr_min_max[i])
    
    return arr
    
