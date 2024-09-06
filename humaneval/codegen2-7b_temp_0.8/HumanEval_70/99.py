
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
    lst = list(lst)
    for i in range(len(lst)):
        swap = lst[i]
        for j in range(i+1, len(lst)):
            if lst[j] < swap:
                lst[j], lst[i] = lst[i], lst[j]
                swap = lst[i]
                break
    return lst
