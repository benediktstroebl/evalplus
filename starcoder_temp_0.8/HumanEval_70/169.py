
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
    # Your code here

    def strange_sort(lst):
        if lst == []:
            return []

        if len(lst) == 1:
            return lst

        a = min(lst)
        b = max(lst)
        c = sorted(set(lst)-{a, b})
        return [a] + strange_sort(c) + [b]

    return strange_sort(lst)
