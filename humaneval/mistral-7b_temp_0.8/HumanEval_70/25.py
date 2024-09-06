
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
        temp_lst = []
        # max = max_of_list(lst)
        # if max is not None:
        #     temp_lst.append(max)
        #     temp_lst += [min(lst)]
        #     temp_lst += strange_sort_list(lst[:-2])
        #     return temp_lst
        return []
