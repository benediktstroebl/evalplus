
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
    def get_ordered_indexes(lst):
        indexes = list(range(len(lst)))
        while indexes:
            min_index = min(indexes)
            max_index = max(indexes)
            yield (min_index, max_index)
            indexes.remove(min_index)
            indexes.remove(max_index)
    result = []
    for min_index, max_index in get_ordered_indexes(lst):
        result.extend([lst[min_index], lst[max_index]])
    return result

