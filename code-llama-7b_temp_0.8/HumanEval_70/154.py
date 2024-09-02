
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
        return lst
    if len(lst) == 1:
        return lst
    if len(lst) == 2:
        return [lst[1], lst[0]]
    lst1 = []
    lst2 = []
    lst3 = []
    lst4 = []
    lst5 = []
    lst6 = []
    lst7 = []
    lst8 = []
    lst9 = []
    lst0 = []
    for i in lst:
        if i == min(lst):
            lst1.append(i)
        elif i == max(lst):
            lst2.append(i)
        elif i < min(lst):
            lst3.append(i)
        elif i > max(lst):
            lst4.append(i)
        elif i == min(lst3):
            lst5.append(i)
        elif i == max(lst3):
            lst6.append(i)
        elif i < min(lst3):
            lst7.append(i)
        elif i > max(lst3):
            lst8.append(i)
        else:
            lst9.append(i)
            lst0.append(i)
    return lst1 + lst2 + lst5 + lst6 + lst0 + lst7 + lst8 + lst9

