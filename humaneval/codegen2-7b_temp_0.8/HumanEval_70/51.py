
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
    lst_sorted = sorted(lst)
    length = len(lst)
    for i in range(1, length+1):
        for j in range(length-i+1):
            if lst_sorted[j] > lst_sorted[j+i]:
                lst_sorted[j], lst_sorted[j+i] = lst_sorted[j+i], lst_sorted[j]
    return lst_s
