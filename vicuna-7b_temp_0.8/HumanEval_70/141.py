
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
    n = len(lst)
    result = []
    for i in range(n):
        min_idx = 0
        max_idx = i
        min_val = lst[i]
        max_val = lst[i]
        for j in range(i+1, n):
            if j == i:
                continue
            if lst[j] < min_val:
                min_idx = j
                min_val = lst[j]
            if lst[j] > max_val:
                max_idx = j
                max_val = lst[j]
        result.append(min_val)
        result.append(max_val)
        result.append(min_idx)
        result.append(max_idx)
    return result
