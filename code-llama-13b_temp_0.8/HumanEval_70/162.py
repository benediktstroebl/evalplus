
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
    output = []

    while lst:
        if len(lst) % 2 == 1:
            output.append(min(lst))
        else:
            output.append(max(lst))
        for i in lst:
            if i != min(lst):
                lst.remove(i)

    return output

