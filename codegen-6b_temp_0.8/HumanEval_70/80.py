
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
        return []

    result = []
    lst.sort()

    for i in xrange(len(lst)):
        if i == 0:
            result.append(lst[i])
        elif i == len(lst)-1:
            result.append(lst[i])
        else:
            if lst[i-1] < lst[i] and lst[i+1] < lst[i]:
                result.append(lst[i])

    return result
