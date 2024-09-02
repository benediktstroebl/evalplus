
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
    if lst == []:
        return []
    elif len(lst) == 1:
        return lst
    elif len(lst) == 2:
        if lst[0] <= lst[1]:
            return lst
        else:
            return [lst[1], lst[0]]
    elif len(lst) == 3:
        lst.sort()
        lst.reverse()
        return lst
    else:
        odd = []
        even = []
        for i in range(len(lst)):
            if i % 2 != 0:
                odd.append(lst[i])
            else:
                even.append(lst[i])
        even.reverse()
        return odd + even

