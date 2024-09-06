
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
    n = len(lst)
    result = []
    for i in range(n):
        left = i
        right = n - i - 1
        result.append(lst[i])
        while right >= 0 and lst[right] >= lst[left]:
            result.insert(0, lst[right])
            right -= 1
    result.extend(lst[left:])
    return result
