
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
    new_list = []
    if lst == []:
        return []
    else:
        min = min(lst)
        max = max(lst)
        while len(lst) > 1:
            new_list.append(min)
            lst.remove(min)
            if lst == []:
                break
            new_list.append(max)
            lst.remove(max)
        new_list += lst
        return new_list
