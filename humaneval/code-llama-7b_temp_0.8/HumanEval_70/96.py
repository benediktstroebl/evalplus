
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
    result = []

    while len(lst) > 0:
        lst = sorted(lst, reverse=True)
        result.append(lst[0])

        min_num = lst[0]
        for i in range(1, len(lst)):
            if min_num > lst[i]:
                lst[i] = lst[i+1]
        lst.pop()
    return result
















