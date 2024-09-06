
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
    i = 0
    while i < len(lst):
        if lst[i] < lst[i+1]:
            j = i
            for k in range(i+1, len(lst)):
                if lst[k] > lst[j]:
                    j = k
            lst[i:j+1] = lst[i:j+1][::-1]
            i = j
    return lst
