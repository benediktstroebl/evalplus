
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

    sorted_lst = sorted(lst)
    final_list = []
    for num in sorted_lst:
        final_list.append(num)
        final_list.append(max(sorted_lst))
        sorted_lst.remove(max(sorted_lst))
    return final_list

