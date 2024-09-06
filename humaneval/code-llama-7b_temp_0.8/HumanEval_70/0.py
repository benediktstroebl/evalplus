
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
        return lst

    if len(lst) == 1:
        return lst

    if len(lst) == 2:
        if lst[0] < lst[1]:
            return lst
        if lst[0] > lst[1]:
            return lst.reverse()

    if len(lst) > 2:
        lst_len = len(lst)
        val_lst = []

        while len(lst) > 0:
            min_val = min(lst)
            max_val = max(lst)
            lst.remove(max_val)
            lst.remove(min_val)
            val_lst.append(min_val)
            val_lst.append(max_val)

        return val_lst





