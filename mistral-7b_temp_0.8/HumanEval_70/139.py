
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

    def sorting(lst):
        if len(lst) == 1:
            return lst
        else:
            min_el = min(lst)
            max_el = max(lst)
            result = [min_el]
            result.extend(sorting(lst - [min_el, max_el]))
            result.append(max_el)
            return result

    return sorting(lst)
