
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
    if lst == []:
        return []
    else:
        small = min(lst)
        big = max(lst)
        new_lst = []
        for i in range(len(lst)):
            lst.remove(small)
            lst.remove(big)
            if i % 2 == 0:
                new_lst.append(small)
                new_lst.append(big)
            else:
                new_lst.append(big)
                new_lst.append(small)
    return new_lst
