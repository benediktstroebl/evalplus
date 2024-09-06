
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
    if lst == []:
        return []
    else:
        min_val = min(lst)
        lst.remove(min_val)
        max_val = max(lst)
        # Ordering strange integers
        lst.append(min_val)
        lst.insert(0, max_val)
        return lst

strange_sort_list([1, 2, 3, 4])
strange_sort_list([5, 5, 5, 5])
strange_sort_list([])
strange_sort_list([1, 1, 1, 1])
strange_sort_list([3, 1, 2, 1, 2, 4, 5, 1, 2, 3])
strange_sort_list([-1, -2, -3, -4])
