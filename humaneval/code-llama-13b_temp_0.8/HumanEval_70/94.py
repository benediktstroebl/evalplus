
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
    n = len(lst)
    if n == 0:
        return []
    else:
        if n%2 == 1:
            half_len = n//2+1
        else:
            half_len = n//2
        head = min(lst)
        tail = max(lst)
        sorted_lst = [head] + [tail]
        for i in range(half_len):
            lst.remove(head)
            lst.remove(tail)
            head = min(lst)
            tail = max(lst)
            sorted_lst += [head, tail]
        return sorted_lst
    
