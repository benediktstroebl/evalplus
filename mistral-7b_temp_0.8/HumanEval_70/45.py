
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
    # Your code goes here
    if not lst:
        return []
    else:
        s=[]
        for i in range(len(lst)):
            if i==0:
                s.append(lst[i])
            elif i%2==0:
                s.append(lst[i])
            else:
                s.insert(0, lst[i])
        return s
