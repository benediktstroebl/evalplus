
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
    result = []
    #max_num = max(lst)
    #min_num = min(lst)
    #print(max_num, min_num)
    lst_length = len(lst)
    for i in range(lst_length):
        min_value = min(lst)
        lst.remove(min_value)
        max_value = max(lst)
        lst.remove(max_value)
        lst.insert(0,min_value)
        lst.append(max_value)
        print(lst)
    return lst
    #if lst_length == 0:
    #    return []
    #else:
    #    result.append(min(lst))
    #    result.append(max(lst))
    #    return result
