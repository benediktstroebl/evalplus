
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
    def get_strange_sort(lst):
        min_value = min(lst)
        remaining_values = [x for x in lst if x!= min_value]
        max_value = max(remaining_values)
        return [min_value] + remaining_values + [max_value]

    return get_strange_sort(lst)
