
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
    def strange(lst):
        l = len(lst)
        lst1 = lst[:]
        if l <= 1:
            return lst
        elif l == 2:
            if lst[0] > lst[1]:
                return [lst[1], lst[0]]
            else:
                return lst
        lst1.sort()
        for i in range(l-2):
            lst1[i+1] = lst[lst1[i]]
        lst1[-1] = lst[lst1[-2]]
        lst1.reverse()
        return lst1
    res = []
    lst2 = lst[:]
    while len(lst2) != 0:
        minn = min(lst2)
        res.append(minn)
        lst2.remove(minn)
        if len(lst2) == 0:
            return res
        lst2 = strange(lst2)


