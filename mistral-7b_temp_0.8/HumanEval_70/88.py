
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
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return lst
    lst_sorted = []
    min_number = min(lst)
    max_number = max(lst)
    if min_number == max_number:
        lst_sorted.append(min_number)
        lst_sorted.extend(lst)
        return lst_sorted
    lst_sorted.append(min_number)
    lst_sorted.append(max_number)
    lst_sorted.extend(lst)
    return lst_sorted
