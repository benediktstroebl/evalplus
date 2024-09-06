
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

    def recurse(index, lst):
        if index == len(lst):
            return lst
        minimum = lst[index]
        maximum = lst[index]
        for idx in range(index + 1, len(lst)):
            if lst[idx] > maximum:
                maximum = lst[idx]
            if lst[idx] < minimum:
                minimum = lst[idx]
        lst[index] = maximum
        lst[index + 1] = minimum
        return recurse(index + 2, lst)

    return recurse(0, lst)

