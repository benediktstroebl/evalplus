
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
    if len(lst) == 0:
        return lst
    result = []
    min_so_far = min(lst)
    for i in range(len(lst)):
        result.append(min_so_far)
        lst.remove(min_so_far)
        if len(lst) == 0:
            return result
        max_so_far = max(lst)
        min_so_far = min(lst)
    return result

assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
assert strange_sort_list([]) == []
assert strange_sort_list([4, 3, 2, 1]) == [1, 2, 3, 4]
assert strange_sort_list([2, 4, 1, 2]) == [2, 1, 2, 4]
