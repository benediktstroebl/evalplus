def strange_sort_list(lst):
    # Ensure the list has at least two elements
    if len(lst) < 2:
        return lst
    
    # Sort the list alternating between the smallest and largest value
    # Start with the smallest value
    sorted_list = [min(lst)]
    # Filter the list to exclude the smallest value
    lst = [x for x in lst if x > sorted_list[0]]
    # Sort the remaining list by the largest value
    sorted_list.extend(sorted(lst, reverse=True))
    # Remove the largest value from the list
    lst = [x for x in lst if x != sorted_list[-1]]
    # Repeat until the list is empty
    return sorted_list