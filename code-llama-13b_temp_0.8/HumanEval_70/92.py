
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
    if len(lst) % 2 == 0:
        min_lst = []
        max_lst = []
        for i in range(0, len(lst)):
            if lst[i] % 2 == 0:
                min_lst.append(lst[i])
            else:
                max_lst.append(lst[i])
        lst.sort()
        return min_lst + max_lst
    else:
        min_lst = []
        max_lst = []
        for i in range(0, len(lst)):
            if lst[i] % 2 == 0:
                min_lst.append(lst[i])
            else:
                max_lst.append(lst[i])
        min_lst.sort()
        max_lst.sort()
        return min_lst + max_lst

