
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
        return []

    sorted_lst = []
    current_min = min(lst)
    current_max = max(lst)

    for n in lst:
        if n == current_min:
            sorted_lst.append(current_max)
            current_max = max(lst)
        elif n == current_max:
            sorted_lst.append(current_min)
            current_min = min(lst)
        else:
            sorted_lst.append(n)

    return sorted_lst

