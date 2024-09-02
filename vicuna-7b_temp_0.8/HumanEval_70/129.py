
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
    k = 0
    for i in range(n):
        if i == n//2:
            k += 1
        if k == 1:
            return lst[i]
        if lst[i] < lst[i+1]:
            lst[i:i+k] = [lst[i]] * k
        else:
            lst[i:i+k] = [lst[i+1]] * k
    return lst
