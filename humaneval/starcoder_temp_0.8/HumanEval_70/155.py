
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
    # This will be the returned list, which we will append to:
    new_list = []
    # This is a list containing the numbers left
    rest_of_list = []

    # First, we get the minimum value, and append it to the new list
    min_val = min(lst)
    new_list.append(min_val)
    # Next, we get all the values that are not equal to min_val:
    for num in lst:
        if num!= min_val:
            rest_of_list.append(num)
    # And sort the list again, and append the new value to the list.
    rest_of_list = sorted(rest_of_list)
    new_list.append(rest_of_list[0])
    # And so on...
    for num in rest_of_list[1:]:
        new_list.append(num)
    return new_list
