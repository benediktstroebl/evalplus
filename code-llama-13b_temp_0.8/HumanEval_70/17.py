
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
    if not lst:
        return lst
    new_lst = []
    odd = True
    while lst:
        new_lst += [min(lst)] if odd else [max(lst)]
        lst = [el for el in lst if el != new_lst[-1]]
        odd = not odd
    return new_lst

