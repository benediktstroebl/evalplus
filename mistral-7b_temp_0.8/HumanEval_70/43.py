
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
    # You can write your code here.
    res = []
    min_ = lst[0]
    max_ = max(lst)
    while lst:
        for i in lst:
            if i == min_:
                res.append(min_)
                lst.remove(i)
                break
        for i in lst:
            if i == max_:
                res.append(max_)
                lst.remove(i)
                break
    return res
