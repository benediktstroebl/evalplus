
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
    elif len(lst) == 1:
        return lst
    elif len(lst) == 2:
        return lst if lst[0] <= lst[1] else [lst[1], lst[0]]
    else:
        sorted_list = [lst[0]]
        index = 1
        while index < len(lst):
            min_value = min(lst[index:])
            for i in range(len(lst) - 1, -1, -1):
                if lst[i] == min_value:
                    lst[i], lst[index] = lst[index], lst[i]
                    break
            sorted_list.append(lst[index])
            index += 1
        return sorted_list

