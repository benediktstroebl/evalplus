
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
    def get_min_max(lst):
        if len(lst) == 1:
            return lst
        return [min(lst), max(lst)]
    
    def strange_sort(lst):
        if lst == []:
            return []
        new_lst = []
        for i in range(len(lst) // 2):
            new_lst += get_min_max(lst)
        return new_lst
    return strange_sort(lst)

