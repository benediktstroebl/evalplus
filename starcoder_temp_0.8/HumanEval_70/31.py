
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
    l = len(lst)
    if l == 0:
        return []
    elif l == 1:
        return lst
    elif l == 2:
        if lst[0] > lst[1]:
            return lst[::-1]
        return lst
    elif l == 3:
        if lst[0] > lst[1]:
            if lst[1] > lst[2]:
                return lst
            elif lst[2] > lst[1]:
                return lst[::-1]
        elif lst[0] > lst[2]:
            return lst
        elif lst[1] > lst[2]:
            return lst
        return lst
    else:
        i = 0
        j = l-1
        k = 0
        while k < l:
            if lst[k] < lst[i]:
                lst[k], lst[i] = lst[i], lst[k]
                i += 1
                k += 1
            elif lst[k] > lst[j]:
                lst[k], lst[j] = lst[j], lst[k]
                j -= 1
            else:
                k += 1
    return lst

