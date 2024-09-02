
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
    if len(lst) == 1:
        return lst

    n = 1
    min_index = 0
    result = []
    while n <= len(lst):
        index_max = min_index
        for i in range(min_index + 1, len(lst)):
            if lst[i] > lst[index_max]:
                index_max = i
        result.append(lst[index_max])
        lst.pop(index_max)
        if n % 2 == 0:
            index_min = 0
            for i in range(0, len(lst)):
                if lst[i] < lst[index_min]:
                    index_min = i
            result.append(lst[index_min])
            lst.pop(index_min)
        n += 1

    return result

