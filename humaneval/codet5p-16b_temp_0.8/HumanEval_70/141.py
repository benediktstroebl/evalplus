
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

    if lst == []:
        return []
    if len(lst) == 1:
        return lst
    maxi = max(lst)
    mini = min(lst)
    sorted_list = [mini]
    unsorted_list = [maxi]
    for i in range(maxi,mini-1,-1):
        un = [n for n in lst if n < i]
        if un == []:
            continue
        sorted_list.append(max(un))
        un = [n for n in lst if n > i]
        if un == []:
            continue
        un = [n for n in lst if n < i]
        un = un[::-1]
        sorted_list += un
    return sorted_list
    

