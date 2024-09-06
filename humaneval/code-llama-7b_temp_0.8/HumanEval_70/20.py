
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
    #STOP = 0

    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return lst
    elif len(lst) == 2:
        if lst[0] > lst[1]:
            return [lst[1], lst[0]]
        else:
            return lst

    i = 0
    while i < len(lst):
        if i == len(lst)-1:
            break
        if lst[i] < lst[i+1]:
            i += 1
        else:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            if i == len(lst)-1:
                break

    i = 0
    while i < len(lst):
        if i == len(lst)-1:
            break
        if lst[i] > lst[i+1]:
            lst[i+1], lst[i] = lst[i], lst[i+1]
            i += 1
        else:
            i += 1

    return lst



