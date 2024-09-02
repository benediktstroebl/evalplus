
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
    lst1 = lst.copy()
    lst1.sort()
    lst2 = lst.copy()
    lst2.sort(reverse=True)
    if len(lst) % 2 == 1:
        lst2 = lst2[1:]
    result = [lst1[0]]
    for i in range(1, len(lst)):
        if i % 2 == 1:
            result.append(lst2[i - 1])
        else:
            result.append(lst1[i])
    return result

