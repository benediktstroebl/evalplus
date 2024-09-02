
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
    result = [lst[0]]
    length_result = len(result)
    for n in lst[1:]:
        if n < result[0]:
            result.insert(0, n)
        elif n > result[length_result - 1]:
            result.append(n)
        else:
            for i, val in enumerate(result):
                if n < val:
                    result.insert(i, n)
                    break
                elif n > result[-1]:
                    result.append(n)
                    break
    return result

