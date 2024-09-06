
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
    sorted_lst = [lst[0]]
    while lst:
        current = lst.pop(0)
        if current > sorted_lst[-1]:
            sorted_lst.append(current)
        else:
            minimum = min(lst)
            lst.remove(minimum)
            sorted_lst.append(minimum)
            maximum = max(lst)
            lst.remove(maximum)
            sorted_lst.append(maximum)
    return sorted_lst

