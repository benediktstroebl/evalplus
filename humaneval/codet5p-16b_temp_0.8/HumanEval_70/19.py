
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

    sorted = sorted(lst)
    print(sorted)
    result = []
    while sorted:
        result.append(sorted[0])
        sorted.remove(sorted[0])
        max = -1
        for x in sorted:
            if x > max:
                max = x
        result.append(max)
        sorted.remove(max)
        min = +1
        for x in sorted:
            if x < min:
                min = x
        result.append(min)
        sorted.remove(min)
    return result

