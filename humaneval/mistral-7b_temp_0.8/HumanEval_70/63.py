
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
    # your code here
    l = len(lst)
    sorted_list = [0] * l

    for i in range(l):
        if i % 2 == 0:
            sorted_list[i] = min(lst)
            lst.remove(min(lst))
        else:
            sorted_list[i] = max(lst)
            lst.remove(max(lst))
    return sorted_list
