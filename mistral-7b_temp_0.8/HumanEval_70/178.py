
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
    lst.sort()
    reversed_lst = lst[::-1]
    index = 0
    while reversed_lst[index] == lst[index]:
        index += 1
    reversed_lst = reversed_lst[:index] + reversed_lst[index:]
    return reversed_lst
