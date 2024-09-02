
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

    # Variant 1 - with for loop
    # result = []
    #
    # for x in range(0, len(lst), 2):
    #     result.append(min(lst))
    #     lst.remove(min(lst))
    #
    # for x in range(1, len(lst), 2):
    #     result.append(max(lst))
    #     lst.remove(max(lst))
    #
    # return result

    # Variant 2 - with while loop
    result = []
    lst_copy = lst.copy()
    while lst:
        result.append(min(lst))
        lst.remove(min(lst))
        result.append(max(lst))
        lst.remove(max(lst))

    return result

