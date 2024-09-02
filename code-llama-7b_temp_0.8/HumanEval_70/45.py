
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
    lst = lst.copy()
    lst.sort()
    lst1 = lst.copy()
    lst.sort(reverse=True)
    lst2 = lst.copy()
    lst.clear()
    while lst1 and lst2:
        lst.append(lst1.pop(0))
        lst.append(lst2.pop())
    return lst + lst1 + lst2

