
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
    # Your code here
    if lst:
        # Get the minimum value in the list.
        # Remove it from the list.
        minimum = min(lst)
        lst.remove(minimum)
        # Get the maximum value in the list.
        # Remove it from the list.
        maximum = max(lst)
        lst.remove(maximum)
        return [minimum] + strange_sort_list(lst) + [maximum]
    else:
        return []
