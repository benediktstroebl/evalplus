
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
    if not lst:
        return []
    result = [lst[0]]
    for x in lst[1:]:
        if x < result[0]:
            result.insert(0, x)
        elif x > result[-1]:
            result.append(x)
        else:
            insert_at = int(len(result) / 2)
            # insert_at is integer but not index
            try:
                result.insert(insert_at, x)
            except IndexError:
                result.append(x)
    return result

