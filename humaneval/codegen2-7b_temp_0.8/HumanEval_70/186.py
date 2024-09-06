
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
    new_lst = lst[:]
    for i in range(len(new_lst)):
        for j in range(i + 1, len(new_lst)):
            if new_lst[i] > new_lst[j]:
                new_lst[i], new_lst[j] = new_lst[j], new_lst[i]
    return new_lst
