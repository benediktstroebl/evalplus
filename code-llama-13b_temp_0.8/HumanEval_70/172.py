
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

    def get_strange(lst):
        if lst:
            return lst.index(min(lst))
        return []

    sorted_lst = []

    while lst:
        sorted_lst.append(lst.pop(get_strange(lst)))

    return sorted_lst

