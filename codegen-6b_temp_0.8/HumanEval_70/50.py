
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
        return lst
    min_val = min(lst)
    max_val = max(lst)
    sorted_lst = [None] * n
    for i in range(n):
        if lst[i] == max_val:
            sorted_lst[i] = lst[-1]
            max_val -= 1
        elif lst[i] == min_val:
            sorted_lst[i] = lst[0]
            min_val += 1
        else:
            sorted_lst[i] = lst[i]
    return sorted_lst

