
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
    lst = sorted(lst, reverse=True)
    print(lst)
    max_num = 0
    min_num = 0
    for x in range(len(lst)-1):
        max_num = max(lst[x], max_num)
        min_num = min(lst[x], min_num)
        lst[x+1] = max_num
        lst[x+2] = min_num
    return lst
