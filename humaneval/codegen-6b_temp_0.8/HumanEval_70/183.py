
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
    if not lst:  return []
    lst.sort()
    l = [lst[0]]
    for i in xrange(1, len(lst)):
        if lst[i] > l[-1]:
            l.append(lst[i])
        else:
            k = -1
            for j in xrange(1, len(l)):
                if lst[i] > l[j] and lst[i] < l[k]:
                    k = j
            l[k] = lst[i]
    return l

