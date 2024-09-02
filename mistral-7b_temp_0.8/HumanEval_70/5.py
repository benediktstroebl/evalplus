
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
    #Your code here
    a=[]
    for i in range(len(lst)-1):
        if lst[i]<lst[i+1]:
            a.append(lst[i])
        else:
            a.append(lst[i+1])
    return a+[lst[-1]]
