
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
    # Handle the case when the input list is empty
    if not lst:
        return []

    # Handle the case when the input list is a single element
    if len(lst) == 1:
        return lst[0]

    # Store the minimum value in the list
    min_value = lst[0]

    # Store the maximum value in the list
    max_value = lst[-1]

    # Store the current index of the current element
    current_index = 0

    # Store the current value
    current_value = lst[current_index]

    # Get the remaining elements
    remaining_elements = lst[current_index+1:]

    # Sort the remaining elements in a strange order
    return sorted(remaining_elements, key=lambda x: (abs(x-min_value), abs(x-max_value)))
