
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
    if len(lst) == 1:
        return lst
    min_num = min(lst)
    result = [min_num]
    for num in lst[1:]:
        if num < min_num:
            result.append(num)
            min_num = num
    result.append(min_num)
    return result

