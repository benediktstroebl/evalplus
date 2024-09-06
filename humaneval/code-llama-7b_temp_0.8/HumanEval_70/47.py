
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

    if len(lst) <= 1:
        return lst

    max_val = lst[0]

    for i in range(1, len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]

    for i in range(0, len(lst)):
        if lst[i] == max_val:
            lst.pop(i)
            lst.append(max_val)
            break

    lst.sort()

    return lst

