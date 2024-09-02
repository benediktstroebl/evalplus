
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
        low = i
        high = n - i - 1
        while low < high:
            result.append(lst[low])
            low += 1
            high -= 1
    result.extend(lst[low+1:high+1])
    return result
