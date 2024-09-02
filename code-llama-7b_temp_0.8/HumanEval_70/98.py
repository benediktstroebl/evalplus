
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

    # This solution is O(N) time
    lst.sort()
    first, second = 0, 0
    while second < len(lst):
        first, second = first + 1, second + 1
        while first < len(lst) and lst[first] == lst[0]:
            first += 1
        while second < len(lst) and lst[second] == lst[-1]:
            second += 1
        if first < second and first < len(lst) and second < len(lst):
            lst[0], lst[-1] = lst[first], lst[second]
            lst[first], lst[second] = lst[second], lst[first]
    return lst
