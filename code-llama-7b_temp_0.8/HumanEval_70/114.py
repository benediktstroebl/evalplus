
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
    elif len(lst) == 1:
        return lst
    else:
        min_list = []
        for i in lst:
            if len(min_list) == 0:
                min_list.append(i)
            else:
                if i <= min_list[0]:
                    min_list.append(i)
        lst = [x for x in lst if x not in min_list]
        max_list = [max(lst)]
        for i in lst:
            if i > max_list[0]:
                max_list.append(i)
        lst = [x for x in lst if x not in max_list]
        min_list.extend(max_list)
        return min_list
