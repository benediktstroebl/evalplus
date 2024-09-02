
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
    new_list = lst
    length = len(new_list)
    for i in range(length-1):
        index = i
        if new_list[i] < new_list[-1]:
            index = -1
        temp = new_list[index]
        j = i
        while j > index:
            new_list[j] = new_list[j-1]
            j -= 1
        new_list[j] = temp
    return new_list
