
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

    if len(lst) <= 1:
        return lst

    sort_lst = sorted(lst)
    odd_idx = len(sort_lst) % 2
    result = [sort_lst[0]]
    for i in range(1, len(sort_lst)):
        result.append(sort_lst[odd_idx * i])
        result.append(sort_lst[1 - odd_idx * i])
    return result
