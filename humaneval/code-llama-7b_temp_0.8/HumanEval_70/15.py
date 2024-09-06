
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

    if len(lst) < 2:
        return lst

    if len(lst) == 2:
        if lst[0] > lst[1]:
            return [lst[1], lst[0]]
        else:
            return lst

    # Create two lists
    # One is the list that can be considered as not empty, the other is the rest of the list
    not_empty_list = [lst[0]]
    lst_without_first_item = lst[1:]

    # Create a list of the maximum and the minimum of the not empty list
    max_min = [max(not_empty_list), min(not_empty_list)]

    # Create a list that contains the maximum and the minimum of the not empty list,
    # and the maximum of the rest of the list
    big_little = max_min + [max(lst_without_first_item)]

    # Create a new list with the minimum, the maximum, the minimum and the maximum of the rest of the list
    lst = [min(lst)] + big_little + [max(lst)]

    # If the length of the list is odd, remove the last element
    if len(lst) % 2 == 1:
        lst.pop()

    return lst
