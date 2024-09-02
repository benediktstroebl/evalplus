
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
    result = [[lst[i]] + [lst[j] for j in range(i+1, n)]
             for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            result[i][j] = max(result[i][j], result[i-1][j])
    return result