
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
    # solution by sifulan
    if len(lst) < 2:
        return lst
    ans = []
    if lst[0] < lst[-1]:
        ans.append(min(lst))
        ans.append(max(lst[1:]))
        ans += sorted(lst[1:])[:-1]
    else:
        ans.append(max(lst))
        ans.append(min(lst[1:]))
        ans += sorted(lst[1:])[:-1]
    return ans

