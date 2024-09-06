
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
    if not lst:
        return lst
    sorted_lst = sorted(lst)
    final_lst = []
    i = 0
    while i < len(lst):
        if i % 2 == 0:
            final_lst.append(sorted_lst[0])
            sorted_lst = sorted_lst[1:]
        else:
            final_lst.append(sorted_lst[-1])
            sorted_lst = sorted_lst[:-1]
        i += 1
    return final_lst

