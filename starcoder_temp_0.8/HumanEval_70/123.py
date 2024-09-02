
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
    # #Method 1
    # def return_strange_sort(lst):
    #     if len(lst) == 0:
    #         return []
    #     elif len(lst) == 1:
    #         return lst
    #     else:
    #         return [lst[0]] + return_strange_sort(sorted(lst[1:]))

    #Method 2
    def return_strange_sort(lst):
        if len(lst) == 0:
            return []
        elif len(lst) == 1:
            return lst
        else:
            return [lst[0]] + return_strange_sort(sorted(lst[1:]))

    return return_strange_sort(lst)

