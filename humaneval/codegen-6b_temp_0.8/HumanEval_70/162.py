
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
    
    from itertools import chain

    new_lst = []

    for i in range(len(lst)):
        if i == 0:
            new_lst.append(min(lst))
        elif i % 2 == 0:
            new_lst.append(lst[i-1])
        else:
            new_lst.append(lst[i-2])

    return list(chain.from_iterable(zip(new_lst, new_lst[1:])))
            
