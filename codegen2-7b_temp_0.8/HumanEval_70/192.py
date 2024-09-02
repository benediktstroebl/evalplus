
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
    import random
    random.shuffle(lst)
    for i in range(0,len(lst)-1):
        for j in range(i+1,len(lst)):
            if lst[i]>lst[j]:
                temp = lst[j]
                lst[j] = lst[i]
                lst[i] = temp
    return lst
    

