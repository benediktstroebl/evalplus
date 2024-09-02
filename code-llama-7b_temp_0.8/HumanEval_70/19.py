
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
    if len(lst) == 0:
        return []
    else:
        temp_lst = lst
        temp_lst.sort()
        result_lst = []
        while len(temp_lst) > 0:
            min_val = temp_lst[0]
            max_val = max(temp_lst[1:])
            result_lst.append(min_val)
            result_lst.append(max_val)
            temp_lst.remove(max_val)
            temp_lst.remove(min_val)
        return result_lst
