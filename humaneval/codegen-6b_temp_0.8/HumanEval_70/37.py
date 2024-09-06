
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
    if len(lst) == 0:
        return lst
    min_value = min(lst)
    sort_list = []
    for i in range(len(lst)):                  # enumerate(lst) == [(0, 1), (1, 2), (2, 3), (3, 4)]
        sort_list.append(lst[i] - min_value)    # here -min_value == 1
    return sort_list
