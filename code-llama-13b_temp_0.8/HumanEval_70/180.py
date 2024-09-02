
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
    # you code here
    new_lst = []
    flag = 0
    while flag < len(lst):
        if flag % 2 == 0:
            new_lst.append(min(lst[flag:]))
        else:
            new_lst.append(max(lst[flag:]))
        flag += 1
    return new_lst

