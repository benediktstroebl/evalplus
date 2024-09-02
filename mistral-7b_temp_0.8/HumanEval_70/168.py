
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

    # Your code here.
    # Best case is O(n) and worst case is O(n^2)
    n = len(lst)
    output = [None] * n
    lst_copy = list(lst)
    i = 0
    while n > 0:
        min_val = min(lst_copy)
        output[i] = min_val
        lst_copy.remove(min_val)
        n -= 1
        i += 1

    return output


