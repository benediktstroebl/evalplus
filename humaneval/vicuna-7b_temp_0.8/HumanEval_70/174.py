
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
    return sorted(lst, key=lambda x: x if x == lst[0] else max(lst[1:]), reverse=True)

print(strange_sort_list([2, 1, 3, 4, 5, 6, 7, 8, 9, 10]))  # [1, 4, 2, 3, 5, 6, 7, 8, 9, 10]
print(strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))  # [1, 4, 2, 3, 5, 6, 7, 8, 9, 10, 11]
print(strange_sort_list([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))  # [1, 4, 2, 3, 5, 6, 7, 8, 9, 10]
print(strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))  # [1, 14, 15, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
