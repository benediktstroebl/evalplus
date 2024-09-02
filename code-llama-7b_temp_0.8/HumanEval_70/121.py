
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

    if len(lst) == 0:
        return lst
    
    sorted_list = []
    smallest = min(lst)
    largest = max(lst)
    lst.remove(smallest)
    lst.remove(largest)

    sorted_list.append(smallest)
    sorted_list.append(largest)
    
    while len(lst) > 0:
        smallest = min(lst)
        sorted_list.append(smallest)
        lst.remove(smallest)

    return sorted_list

