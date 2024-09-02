
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
    new_list=[]
    for i in range(0,len(lst)):
        if(i==0):
            new_list.append(lst[i])
        else:
            index=0
            for j in range(i):
                if(lst[index]>lst[i]):
                    index+=1
            if(i==len(lst)-1):
                new_list.append(lst[index])
            else:
                new_list.append(lst[index])
                new_list.append(lst[i])
    return new_list

