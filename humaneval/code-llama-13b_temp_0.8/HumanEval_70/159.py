
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
    if len(lst) == 0:
        return lst
    l1 = []
    l2 = []
    for i in lst:
        if i < 0:
            l1.append(i)
        else:
            l2.append(i)
    l1 = sorted(l1)
    l2 = sorted(l2)
    if len(l1) > len(l2):
        k = len(l1) - len(l2)
        for i in range(k):
            l2.append(min(l1))
            l1.remove(min(l1))
    else:
        k = len(l2) - len(l1)
        for i in range(k):
            l1.append(max(l2))
            l2.remove(max(l2))
    if len(l1) == len(l2):
        for i in range(len(l1)):
            l1[i], l2[i] = min(l1[i], l2[i]), max(l1[i], l2[i])
    else:
        if len(l1) > len(l2):
            k = len(l1) - len(l2)
            for i in range(k):
                l2.append(min(l1))
                l1.remove(min(l1))
        else:
            k = len(l2) - len(l1)
            for i in range(k):
                l1.append(max(l2))
                l2.remove(max(l2))
        for i in range(len(l1)):
            l1[i], l2[i] = min(l1[i], l2[i]), max(l1[i], l2[i])
    return l1 + l2

