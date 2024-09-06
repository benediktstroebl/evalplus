
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
    # your code here
    n = len(lst)
    new_list = []

    for i in range(0, n, 2):
        min_val = min(lst)
        max_val = max(lst)
        new_list.append(min_val)
        new_list.append(max_val)
        lst.remove(min_val)
        lst.remove(max_val)

    return new_list

