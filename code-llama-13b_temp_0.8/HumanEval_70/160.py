
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
    def _strange_sort_list(lst, min_or_max_value):
        sorted_list = []
        while lst:
            if min_or_max_value == 'min':
                min_value = min(lst)
                sorted_list.append(min_value)
                lst.remove(min_value)
            else:
                max_value = max(lst)
                sorted_list.append(max_value)
                lst.remove(max_value)
            min_or_max_value = 'min' if min_or_max_value == 'max' else 'max'
        return sorted_list
    return _strange_sort_list(lst, 'min')

