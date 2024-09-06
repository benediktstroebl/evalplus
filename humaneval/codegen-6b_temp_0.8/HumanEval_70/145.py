
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
        return lst
    min_value = min(lst)
    min_index = lst.index(min_value)
    lst[min_index] = max(lst)
    lst[lst.index(max(lst))] = min_value
    return lst


'''
Exemplary tests:
assert strange_sort_list([1]) == [1]
assert strange_sort_list([1, 2]) == [1, 2]
assert strange_sort_list([1, 2, 3]) == [1, 3, 2]
assert strange_sort_list([4, 5, 3]) == [3, 4, 5]
assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
assert strange_sort_list([1, 2, 3, 4, 6, 5]) == [1, 5, 6, 4, 3, 2]
assert strange_sort_list([]) == []
assert strange_sort_list([4, 1, 2, 3]) == [1, 4, 2, 3]
assert strange_sort_list([2, 3, 1]) == [1, 3, 2]
assert strange_sort_list([1, 3, 2]) == [1, 2, 3]
'''
