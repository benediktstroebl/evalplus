
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
    #return sorted(lst, reverse=True)
    # return sorted(lst, key=len)
    # return sorted(lst, key=len, reverse=True)
    #return sorted(lst, key=lambda x: x%2)
    #return sorted(lst, key=lambda x: x % 2, reverse=True)
    # return sorted(lst, key=lambda x: x != min(lst))
    # return sorted(lst, key=lambda x: (x != min(lst), x))
    if len(lst) == 0:
        return []
    return [lst[0]] + [min(lst[1:])] + [lst[0]] + [max(lst[1:])] + strange_sort_list(lst[1:])

