
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
    if len(lst) < 2:
        return lst
    n = len(lst)
    temp = lst[0]
    for i in range(n-1):
        if temp >= lst[n-i-1]:
            temp = lst[n-i-1]
            lst[n-i-1] = lst[0]
            lst[0] = temp
            return lst
    lst.reverse()
    return lst

