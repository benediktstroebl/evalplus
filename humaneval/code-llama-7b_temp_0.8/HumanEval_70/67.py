
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
    def min_value(num):
        for value in lst:
            if value == num:
                return num

    result = []
    if lst == []:
        return lst
    else:
        num = min(lst)
        for i in lst:
            if i == num:
                lst.remove(i)
        lst = sorted(lst)
        lst.insert(0,num)
        lst.reverse()
        return lst

