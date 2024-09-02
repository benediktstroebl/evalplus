
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
    res = [0] * n
    left = 0
    right = n-1
    while left < right:
        for i in range(left,right):
            if lst[i] < lst[left]:
                res[left] = lst[i]
                left += 1
                break
        for i in range(right-1,left,-1):
            if lst[i] < lst[right]:
                res[right] = lst[i]
                right -= 1
                break
    res[left] = lst[left]
    res[right] = lst[right]
    return res
