
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
    def strange_sort_list_recursive(numbers, result):
        if not numbers:
            return result
        min_num = min(numbers)
        result.append(min_num)
        numbers.remove(min_num)
        return strange_sort_list_recursive(numbers, result)

    return strange_sort_list_recursive(lst, [])
