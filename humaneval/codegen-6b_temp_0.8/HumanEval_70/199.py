
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
    if lst:
        if len(lst) == 1:
            return lst
        min_max = min(lst)
        lst.remove(min_max)
        lst.sort()
        lst.insert(0, min_max)
        return lst
    return []


assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
assert strange_sort_list([]) == []
assert strange_sort_list([1]) == [1]
assert strange_sort_list([2, 1]) == [1, 2]
assert strange_sort_list([1, 2, 2, 3]) == [1, 2, 2, 3]
assert strange_sort_list([1, 1, 2, 2, 3, 3, 4, 4]) == [1, 1, 2, 2, 3, 3, 4, 4]

