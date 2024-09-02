
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

    # splitting list in two parts
    split_index = len(lst) // 2
    left = lst[:split_index]
    right = lst[split_index:]

    result = []
    # infinite loop
    while len(left) > 0 and len(right) > 0:
        result.append(min(left))
        result.append(max(right))
        left.remove(min(left))
        right.remove(max(right))

    if len(left) == 0:
        result += right
    else:
        result += left
    return result

