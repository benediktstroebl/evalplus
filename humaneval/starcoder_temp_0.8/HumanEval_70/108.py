
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
    result = []
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return lst
    if len(lst) == 2:
        if lst[0] < lst[1]:
            return [lst[0], lst[1]]
        else:
            return [lst[1], lst[0]]
    if len(lst) > 2:
        smallest = lst[0]
        for i in lst:
            if i < smallest:
                smallest = i
        result.append(smallest)
        lst.remove(smallest)
        largest = lst[-1]
        for i in lst:
            if i > largest:
                largest = i
        result.append(largest)
        lst.remove(largest)
        result += strange_sort_list(lst)
    return result
