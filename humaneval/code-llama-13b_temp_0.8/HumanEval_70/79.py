
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

    even_sort = sorted(lst)
    odd_sort = sorted(lst, reverse=True)

    if len(lst) % 2:
        return [odd_sort[i] if i % 2 else even_sort[i] for i in range(len(lst))]
    return [even_sort[i] if i % 2 else odd_sort[i] for i in range(len(lst))]

