
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
    # lst = [5, 5, 5, 5]
    # lst = [1, 2, 3, 4]
    # lst = []
    # lst = [1, 2, 3]
    # lst = [1]
    # lst = [1, 2]
    # lst = [1, 2, 3, 4]
    # lst = [1, 2, 5, 5]

    lst.sort()

    sorted_list = []
    start_index = 0
    end_index = len(lst) - 1

    while end_index > start_index:
        num = lst[start_index]
        end_index = lst.index(num)
        sorted_list.append(num)
        end_index -= 1
        start_index += 1

    sorted_list.append(lst[end_index])
    return sorted_list

