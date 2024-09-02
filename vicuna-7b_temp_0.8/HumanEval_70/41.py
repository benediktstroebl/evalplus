
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
    lst_len = len(lst)
    result = []
    for i in range(lst_len):
        if i == 0:
            result.append(lst[i])
        elif i == lst_len - 1:
            result.append(lst[i])
        else:
            j = (i + 1) % lst_len
            result.append(lst[i])
            result.append(lst[j])
    return result
