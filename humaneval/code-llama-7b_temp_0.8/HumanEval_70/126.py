
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
    list_len = len(lst)
    if list_len == 0:
        return []
    lst.sort()
    #print(lst)
    strange_lst = [lst[0]]
    for i in range(list_len):
        #print(i, lst[i], lst[list_len - 1 - i])
        if i % 2 != 0:
            strange_lst.append(lst[list_len - 1 - i])
        else:
            strange_lst.append(lst[i])
    return strange_lst


