
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

    if lst:
        odd, even = [], []
        for i, num in enumerate(lst):
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        even.sort()
        odd.sort(reverse=True)
        res = []
        while even and odd:
            res += [even.pop(), odd.pop()]
        if odd:
            res += odd
        if even:
            res += even
        return res
    return lst

