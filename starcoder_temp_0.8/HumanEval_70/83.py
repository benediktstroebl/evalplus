
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
    new_lst = []
    for i in range(len(lst)):
        min_value = min(lst)
        new_lst.append(min_value)
        lst.remove(min_value)
    for i in range(len(lst)):
        max_value = max(lst)
        new_lst.append(max_value)
        lst.remove(max_value)
    return new_lst
