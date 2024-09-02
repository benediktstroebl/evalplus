
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
    # If the list is empty, return the empty list.
    if not lst:
        return lst

    # Store the list elements in tuple.
    x = tuple(lst)

    # Put the sorted list elements in array.
    array = []
    # For each element in the list,
    for element in x:
        # Store the element in array.
        array.append(element)
        # Sort the array in descending order.
        array.sort(reverse=True)

    # Return the sorted list elements in array.
    return array

