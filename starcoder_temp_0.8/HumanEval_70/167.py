
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
    if len(lst) == 1:
        return lst

    if len(lst) == 2:
        if lst[0] > lst[1]:
            return [lst[1], lst[0]]
        return lst

    min_index = 0
    min_value = lst[0]
    for i in range(len(lst)):
        if lst[i] < min_value:
            min_value = lst[i]
            min_index = i

    remaining_elements = []
    for i in range(len(lst)):
        if i == min_index:
            continue
        remaining_elements.append(lst[i])

    remaining_elements = strange_sort_list(remaining_elements)

    return remaining_elements + [lst[min_index]] + remaining_elements[::-1]

