
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
    # Your code here
    if len(lst) == 0:
        return []

    s = sorted(lst)
    result = []

    #min
    result.append(s[0])
    s.remove(s[0])

    #max
    result.append(s[-1])
    s.remove(s[-1])

    #min
    result.append(s[0])
    s.remove(s[0])

    #max
    result.append(s[-1])
    s.remove(s[-1])

    return result
