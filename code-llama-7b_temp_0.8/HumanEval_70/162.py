
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
    if not lst:
        return []
    result = []
    min_val = lst[0]
    max_val = lst[0]
    lst.pop(0)
    for i in lst:
        if i < min_val:
            min_val = i
        if i > max_val:
            max_val = i
    result.append(min_val)
    result.append(max_val)
    if min_val != max_val:
        result += strange_sort_list(lst)
    return result

