
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
    # Create a new list to store the sorted list
    sorted_lst = []

    # Start with the minimum value
    minimum = lst[0]
    # Add the minimum value to the sorted list
    sorted_lst.append(minimum)

    # Find the maximum of the remaining integers
    max_value = sorted_lst[-1]
    # Add the maximum value to the sorted list
    sorted_lst.append(max_value)

    # Repeat the process with the remaining integers
    for value in lst[1:]:
        # Find the minimum of the remaining values
        min_value = sorted_lst[-1]
        # Add the minimum value to the sorted list
        sorted_lst.append(min_value)

    # Repeat the process with the remaining values
    for value in lst[2:]:
        # Find the maximum of the remaining values
        max_value = sorted_lst[-1]
        # Add the maximum value to the sorted list
        sorted_lst.append(max_value)

    # Return the sorted list
    return sorted_lst
