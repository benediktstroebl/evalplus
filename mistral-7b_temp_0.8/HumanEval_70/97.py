
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
    temp = 0

    for i in lst:
        if not result:
            result.append(i)

        else:
            if temp > i:
                result.insert(0, i)
                temp = i
            else:
                result.append(i)

    return result
