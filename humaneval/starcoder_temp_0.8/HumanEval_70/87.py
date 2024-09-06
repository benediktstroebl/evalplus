
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

    if len(lst) == 0:
        return result

    if len(lst) == 1:
        return [lst[0]]

    if len(lst) == 2:
        if lst[0] > lst[1]:
            return [lst[1], lst[0]]

        return lst

    for i in range(len(lst)):
        if i == 0:
            result.append(min(lst))
        elif i % 2 == 0:
            result.append(max(lst))
        else:
            result.append(min(lst))

        lst.remove(result[-1])

    return result
