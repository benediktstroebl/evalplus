
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
    else:
        min_value = min(lst)
        min_indices = [i for i in range(len(lst)) if lst[i] == min_value]
        return lst[min_indices[-1]] + lst[min_indices[0]:] + lst[:min_indices[0]]

