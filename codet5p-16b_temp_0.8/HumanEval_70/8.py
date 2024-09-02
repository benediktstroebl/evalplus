
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

    lst.sort()

    for i in range(len(lst)):
        if i % 2 == 0:
            lst[i] = min(lst[i::-1])
        else:
            lst[i] = max(lst[i::-1])

    return lst

