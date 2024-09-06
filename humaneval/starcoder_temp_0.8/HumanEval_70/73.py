
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

    new_lst = []
    if len(lst) == 0:
        return new_lst
    else:
        for i in range(len(lst)):
            if i == 0:
                new_lst.append(min(lst))
                lst.remove(min(lst))
            elif i == len(lst)-1:
                new_lst.append(max(lst))
                lst.remove(max(lst))
            else:
                new_lst.append(min(lst))
                lst.remove(min(lst))
        return new_lst

