
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
    n = len(lst)
    for i in range(n):
        smallest = i
        max_i = i
        for j in range(i+1, n):
            if lst[j] > lst[smallest]:
                smallest = j
        lst[smallest], lst[max_i] = lst[max_i], lst[smallest]
    return lst
