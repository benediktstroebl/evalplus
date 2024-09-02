
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
    # your code here
    if len(lst)==0:
        return []
    if len(lst)==1:
        return lst
    max=lst[0]
    min=lst[0]
    x=0
    y=len(lst)-1
    for i in lst:
        if i>max:
            max=i
            x=lst.index(i)
        if i<min:
            min=i
            y=lst.index(i)
    lst.pop(x)
    lst.pop(y)
    lst.insert(x,min)
    lst.insert(y,max)
    return lst
