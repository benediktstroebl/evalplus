
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
    # assert (type(lst) is list)
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return lst
    else:
        sorted_lst = []
        min_index = None
        max_index = None
        min_val = lst[0]
        max_val = lst[0]
        for i in range(0, len(lst)):
            if lst[i] < min_val:
                min_val = lst[i]
                min_index = i
            if lst[i] > max_val:
                max_val = lst[i]
                max_index = i
        sorted_lst.append(max_val)
        sorted_lst.append(min_val)
        indices = [min_index, max_index]
        for i in range(0, 2):
            for j in range(indices[i]+1, len(lst)):
                if lst[j] < lst[indices[i]]:
                    indices[i] = j
        if indices[0] == min_index:
            sorted_lst.append(lst[indices[1]])
            sorted_lst.append(lst[indices[0]])
        else:
            sorted_lst.append(lst[indices[0]])
            sorted_lst.append(lst[indices[1]])
        return sorted_lst
