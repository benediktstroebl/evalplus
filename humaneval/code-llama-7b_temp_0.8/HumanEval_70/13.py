
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
    # Load in all data into a list
    loaded_lst = []
    # Loop through each item in list, append to new list
    for num in lst:
        loaded_lst.append(num)
    # List to hold sorted values
    sorted_lst = []
    # While list isn't empty
    while loaded_lst:
        # Save min value to sorted list
        sorted_lst.append(min(loaded_lst))
        # Remove value from loaded list
        loaded_lst.remove(min(loaded_lst))
        # Save max value to sorted list
        sorted_lst.append(max(loaded_lst))
        # Remove value from loaded list
        loaded_lst.remove(max(loaded_lst))
        # Save min value to sorted list
        sorted_lst.append(min(loaded_lst))
        # Remove value from loaded list
        loaded_lst.remove(min(loaded_lst))
    # Return sorted list
    return sorted_lst
