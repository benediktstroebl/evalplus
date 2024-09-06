
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
    arr = []
    i = 1
    while lst:
        m = min(lst)
        arr.append(m)
        lst.remove(m)
        if i % 2 != 0:
            arr.append(max(lst))
        else:
            arr.append(min(lst))
        lst.remove(arr[-1])
        i += 1
    return arr
    
    

