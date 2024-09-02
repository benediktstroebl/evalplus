
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

    if len(lst) < 2:
        return lst

    result = []
    for i in range(len(lst)):
        j = i
        while lst[j] == lst[j - 1]:
            j += 1
            if j >= len(lst):
                break

        if j >= len(lst):
            break

        result.append(lst[j])
        for k in range(j + 1, len(lst)):
            lst[k - 1] = lst[k]

    result.append(lst[j])

    while len(lst) < len(result):
        lst.append(lst[-1])

    return result

