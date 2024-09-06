
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
    #strange = []
    #for x in range(len(lst)):
        #if x % 2 == 0:
            #strange.append(lst[x])
        #else:
            #strange.append(max(lst))
    #return strange
    return list(reversed(sorted(lst)))
