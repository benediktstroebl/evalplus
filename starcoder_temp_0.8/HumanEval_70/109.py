
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

    sorted_lst = []
    min_num = min(lst)
    max_num = max(lst)

    while sorted_lst!= lst:
        while min_num in lst:
            sorted_lst.append(min_num)
            lst.remove(min_num)
        while max_num in lst:
            sorted_lst.append(max_num)
            lst.remove(max_num)
        min_num = min(lst)
        max_num = max(lst)
        if sorted_lst == lst:
            break

    return sorted_lst
