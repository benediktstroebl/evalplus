
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

    def swap(i, j):
        lst[i], lst[j] = lst[j], lst[i]

    def sort_strange(lst):
        '''
        Given a list, returns list in strange order
        '''
        if len(lst) == 0 or len(lst) == 1:
            return lst
        if len(lst) == 2:
            if lst[1] < lst[0]:
                swap(0, 1)
                return lst
            return lst
        index_min = 0
        index_max = 0
        for i in range(1, len(lst)):
            if lst[i] < lst[index_min]:
                index_min = i
            if lst[i] > lst[index_max]:
                index_max = i

        return sort_strange(lst[:index_min] + [lst[index_min]] +
                            lst[index_min + 1:index_max] +
                            [lst[index
