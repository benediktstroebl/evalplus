
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

    if len(lst) == 1:
        return lst

    # create a new list from the original with no duplicates
    new_list = []
    for num in lst:
        if num not in new_list:
            new_list.append(num)
    print(new_list)

    # return a list that is of the same length, but in a different order
    new_list_2 = []
    for num in new_list:
        if num == min(new_list):
            new_list_2.append(num)
            new_list.remove(min(new_list))
        elif num == max(new_list):
            new_list_2.append(num)
            new_list.remove(max(new_list))
        else:
            new_list_2.append(num)
    return new_list_2
