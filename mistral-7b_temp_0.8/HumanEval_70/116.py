
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

    # if there is no element in the list, return an empty list
    if not lst:
        return lst
    # if there is only one element in the list, return the list
    elif len(lst) == 1:
        return lst

    # create a new empty list to store the sorted elements
    sorted_lst = []

    # initialize the minimum and maximum values
    min_value = min(lst)
    max_value = max(lst)

    # iterate through the list
    for element in lst:
        # if the element is the minimum value, append it to the sorted list
        if element == min_value:
            sorted_lst.append(element)
            min_value = max(lst)
        # if the element is the maximum value, append it to the sorted list
        elif element == max_value:
            sorted_lst.append(element)
            max_value = min(lst)
        # if the element is not the minimum or maximum value, append it to the sorted list
        else:
            sorted_lst.append(element)

