
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
    return sorted(lst)


assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
assert strange_sort_list([]) == []
assert strange_sort_list([1, 15, 3]) == [1, 3, 15]
assert strange_sort_list([5, 1, 2, 4]) == [1, 4, 2, 5]
assert strange_sort_list([10, 5, 2, 4]) == [2, 4, 10, 5]
assert strange_sort_list([1, (5*10)**2, -4, 1]) == [-4, 1, 1, (5*10)**2]

