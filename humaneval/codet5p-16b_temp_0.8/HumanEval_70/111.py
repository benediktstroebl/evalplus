
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

    if len(lst) <= 1:
        return lst
    
    ordered_lst = sorted(lst)
    print(ordered_lst)
    swap_list = []
    i = 0
    while i < len(ordered_lst):
        if i % 2 == 0:
            swap_list.append(ordered_lst[i])
        i += 1
    ordered_lst = ordered_lst[::-1]
    for i in range(len(lst)):
        if i % 2 == 1:
            swap_list.append(ordered_lst[i])

    return swap_list
