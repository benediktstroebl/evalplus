
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
    if n == 0:
        return []
    else:
        pivot = lst[0]
        for i in range(1, n):
            for j in range(i):
                if lst[j] >= pivot:
                    lst[i], lst[j] = lst[j], lst[i]
        return lst

lst = [100, 20, 30, 40, 50, 60]
