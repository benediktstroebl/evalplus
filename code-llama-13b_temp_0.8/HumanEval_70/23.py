
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

    if not lst:
        return []

    # Find max and min values in the list.
    max_value = max(lst)
    min_value = min(lst)

    new_list = []
    odd = True

    # While there are elements in the original list.
    while lst:

        # Check if the element in list is greater than or equal to the current min value
        # and less than or equal to the current max value.
        for i in lst:

            if odd:
                # If greater than or equal to current min value
                if i >= min_value:

                    # Add that element to the new list.
                    new_list.append(i)

                    # Remove that element from the original list.
                    lst.remove(i)

            else:
                # If less than or equal to current max value
                if i <= max_value:

                    # Add that element to the new list.
                    new_list.append(i)

                    # Remove that element from the original list.
                    lst.remove(i)

        # Update odd value.
        odd = not odd

        # Update min/max values.
        if lst:
            min_value = min(lst)
            max_value = max(lst)

    return new_list

