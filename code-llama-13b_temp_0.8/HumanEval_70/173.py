
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

    if len(lst) == 0:
        return lst

    def min_index(lst):
        """
        return index of minimum in lst
        """
        min_index = 0
        for i in range(1, len(lst)):
            if lst[i] < lst[min_index]:
                min_index = i
        return min_index

    def max_index(lst):
        """
        return index of maximum in lst
        """
        max_index = 0
        for i in range(1, len(lst)):
            if lst[i] > lst[max_index]:
                max_index = i
        return max_index

    sorted_list = []
    while lst:
        sorted_list.append(lst.pop(min_index(lst)))
        if lst:
            sorted_list.append(lst.pop(max_index(lst)))

    return sorted_list

