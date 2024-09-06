
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
    if not lst:
        return []
    n = len(lst)
    result = []
    for i in range(n):
        min_val = lst[i]
        max_val = n - i - 1
        min_index = 0
        max_index = n - 1
        for j in range(i, n):
            if j < i:
                val = lst[j]
                if val <= max_val:
                    max_index = j
                    max_val = val
        for j in range(i, n):
            val = lst[j]
            if val <= min_val:
                min_index = j
                min_val = val
        result.insert(0, min_val)
        result.insert(n - min_index - 1, max_val)
        result.insert(n - min_index - 2, min_val)
        result.insert(n - 1, max_val)
    return result
