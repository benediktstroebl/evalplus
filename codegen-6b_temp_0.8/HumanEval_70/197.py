
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
    # Your code, hint:
    # 1) Find the minimum value
    # 2) Find the maximum value
    # 3) Sort the list

    if len(lst)==0:
        return []

    min_value = min(lst)
    max_value = max(lst)
    new = sorted(lst)
    lst = []
    for i in range(min_value, max_value + 1):
        lst.append(i)
    return lst
