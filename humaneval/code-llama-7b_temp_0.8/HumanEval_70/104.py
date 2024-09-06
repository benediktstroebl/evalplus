
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
    if lst == []:
        return lst
    lst2 = [min(lst)]
    lst.remove(min(lst))
    lst3 = [max(lst)]
    lst.remove(max(lst))
    lst4 = strange_sort_list(lst)
    return lst2 + lst3 + lst4
