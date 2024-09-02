
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
    else:
        odd = []
        even = []
        for i in range(0, len(lst)):
            if i % 2 == 0:
                even.append(lst[i])
            else:
                odd.append(lst[i])
        even.sort()
        odd.sort()
        return even + odd

