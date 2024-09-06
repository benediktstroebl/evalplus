
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
    def pairwise(lst):
        """
        Yield (x, y) from lst such that x and y are consecutive elements.
        """
        for i in range(0, len(lst), 1):
            yield lst[i], lst[i+1]

    for i in range(0, len(lst)):
        if i == 0:
            yield lst[i], lst[i]
        elif i == 1:
            yield lst[i], lst[i-1]
        else:
            yield lst[i], lst[i-1], lst[i]

lst = [1, 2, 3, 4]
print(strange_sort_list(lst))
