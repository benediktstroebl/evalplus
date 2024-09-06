
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
    if n < 2:
        return lst
    else:
        min_i = 0
        max_i = n - 1

        for i in range(1, n):
            if lst[i] <= lst[max_i]:
                break
            else:
                max_i -= 1

        for i in range(n-1, 0, -1):
            if lst[i] >= lst[min_i]:
                break
            else:
                min_i += 1
            
        lst[min_i], lst[max_i] = lst[max_i], lst[min_i] 
        if min_i > 1:
            strange_sort_list(lst[:-1])
        if max_i < n - 2:
            strange_sort_list(lst[1:])
        return lst

