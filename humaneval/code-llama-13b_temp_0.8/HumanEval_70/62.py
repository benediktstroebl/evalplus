
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
    def compare_strange(x, y):
        if x in new_lst:
            return -1
        else:
            return 1

    new_lst = []
    new_lst_max = []
    for _ in range(len(lst)):
        new_lst.append(min(lst))
        lst.pop(lst.index(min(lst)))
        new_lst_max.append(max(lst))
        lst.pop(lst.index(max(lst)))

    new_lst.reverse()
    new_lst_max.reverse()
    new_lst = new_lst + new_lst_max
    return new_lst
