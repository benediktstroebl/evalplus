
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

    result = []
    if lst == []:
        return []
    else:
        while lst!= []:
            mini = lst[0]
            maxi = lst[0]
            for x in lst:
                if x > maxi:
                    maxi = x
                elif x < mini:
                    mini = x
            result.append(mini)
            lst.remove(mini)
            result.append(maxi)
            lst.remove(maxi)
        return result
