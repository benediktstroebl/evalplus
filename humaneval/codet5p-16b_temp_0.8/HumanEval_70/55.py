
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

    out_lst = []
    for index in range(len(lst)):
        temp_lst = [x for x in lst if x < lst[index]]
        out_lst.extend(temp_lst)
        lst.remove(temp_lst[-1])
        out_lst.append(lst[index])
    return out_lst

