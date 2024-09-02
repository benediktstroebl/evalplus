
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
    if lst:
        smallest = min(lst)
        new_lst = [smallest]
        for n in lst:
            if n < smallest:
                new_lst.append(n)
        lst = new_lst
        lst.append(smallest)
        return lst
    else:
        return []

