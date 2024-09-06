def strange_sort_list(lst):
    """
    Do a strange sort of the list, returning it in reverse sorted order.

    Args:
        lst (list): List of integers

    Returns:
        list: Strange sorted list
    """
    min_found = len(lst)
    max_found = -1
    strange_sorted_list = []

    for num in lst:
        if num == max_found:
            # If we've already found the max, add the min of the remaining list
            strange_sorted_list.append(min(lst[len(strange_sorted_list):]))
            break
        elif num == min_found:
            # If we've already found the min, add the max of the remaining list
            strange_sorted_list.append(max(lst[len(strange_sorted_list):]))
            break
        elif num > max_found:
            # If we haven't found the max yet, add the max
            max_found = num
            strange_sorted_list.append(max_found)
        elif num < min_found:
            # If we haven't found the min yet, add the min
            min_found = num
            strange_sorted_list.append(min_found)
    return strange_sorted_list