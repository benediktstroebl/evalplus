
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

    current_list = sorted(lst)

    while len(current_list) > 0:
        new_list = []

        for i in range(len(current_list)):
            new_list.append(current_list[-1 - i])

        new_list.append(current_list[0])
        current_list = new_list

    return current_list




