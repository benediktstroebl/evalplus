
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
    def helper(l, r):
        if l > r:
            return
        lst[l], lst[r] = lst[r], lst[l]
        helper(l + 1, r - 1)
        helper(l, r - 1)
        helper(l + 1, r)

    helper(0, len(lst) - 1)
    return lst

