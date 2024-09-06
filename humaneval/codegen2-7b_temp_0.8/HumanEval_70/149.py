
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
    sort_lst = []
    for num in lst:
        if len(sort_lst) == 0:
            sort_lst.append(num)
        else:
            if num < sort_lst[-1]:
                sort_lst.append(num)
            else:
                sort_lst.insert(0, num)
    return sort_lst
