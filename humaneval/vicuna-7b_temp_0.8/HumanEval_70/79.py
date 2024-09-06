
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
    result = [[0] * (n+1) for _ in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            result[i][j] = min(result[i][j], result[i-1][j-1] + result[i-1][j]+ result[i][j-1])
    return result