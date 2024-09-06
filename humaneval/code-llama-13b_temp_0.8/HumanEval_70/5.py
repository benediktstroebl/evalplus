
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
    if lst:
        a = lst[:]
        a.sort()
        lst = [a[0]]
        for i in range(1, len(a), 2):
            lst.append(a[i])
        for i in range(2, len(a), 2):
            lst.append(a[i])
        return lst
    return lst

