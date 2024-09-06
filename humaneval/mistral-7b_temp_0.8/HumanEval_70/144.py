
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
    # Create a sorted list, and a tuple for the size of the list
    sorted_list = sorted(lst)
    list_size = len(sorted_list)
    # Create a list of the same size as sorted_list, to hold the sorted list
    result = []
    # Add a counter to keep track of the index of the sorted_list
    counter = 0
    # Create a variable to hold the highest number
    highest = sorted_list[0]
    # Create a variable to hold the lowest number
    lowest = sorted_list[0]
    # Loop through the sorted_list, and append the highest or lowest number to result
    for i in range(list_size):
        if counter == list_size - 1:
            result.append(sorted_list[i])
            counter = 0
            highest = sorted_list[0]
            lowest = sorted_list[0]
        elif sorted_list[i] == highest:
            highest = sorted_list[i]
            result.append(highest)
            counter += 1
            continue
        elif sorted
