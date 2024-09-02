
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
    # TODO: Write your code here
    if not lst:
        return lst
    else:
        max_index = len(lst) - 1
        new_lst = []
        for i in range(len(lst)):
            new_lst.append(lst[max_index])
            max_index -= 1
            if max_index >= 0:
                new_lst.append(lst[0])
                lst.pop(0)
        return new_lst

