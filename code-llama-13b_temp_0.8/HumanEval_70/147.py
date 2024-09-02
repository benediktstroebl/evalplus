
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

    def sort(lst):
        if lst == []:
            return []
        elif len(lst) == 1:
            return lst
        else:
            min_max = lst[:2]
            return [min_max[min(min_max)]] + sort(lst[2:]) + [min_max[max(min_max)]]

    return sort(lst)

