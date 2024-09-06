def strange_sort_list(lst):
    # Ensure the list has at least one element
    if not lst:
        return lst
    
    # Sort the list in the specified order
    sorted_list = [min(lst)]
    for i in range(len(lst) - 2):
        # Remove the maximum value from the current list
        max_val = max(lst[i+1:])
        sorted_list.append(max_val)
    return sorted_list