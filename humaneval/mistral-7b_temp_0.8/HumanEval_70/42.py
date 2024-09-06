
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
    # Your code goes here
    max_list = []
    min_list = []
    for i in lst:
        if i not in max_list:
            max_list.append(i)
        if i not in min_list:
            min_list.append(i)
    min_list.sort()
    max_list.sort(reverse = True)
    return min_list + max_list
