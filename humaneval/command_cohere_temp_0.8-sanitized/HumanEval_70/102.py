def strange_sort_list(lst):
    """
    Do a strange sort of a list, namely return the minimum value,
    then the maximum of the remaining integers, then the minimum, and so on.
    """
    # Initialize the variables to be the first value of the list and its index
    min_val = lst[0]
    min_idx = 0
    new_lst = [min_val]
    # Iterate through the list
    for i in range(len(lst)):
        # If the current value is less than the current minimum, set it as the new minimum
        if lst[i] < min_val:
            min_val = lst[i]
            min_idx = i
        # If the current index is the minimum index, append the maximum value to the new list
        elif i == min_idx:
            new_lst.append(max(lst))
        # Otherwise, move to the next index in the main list
        else:
            new_lst.append(min_val)
    # Return the strange sorted list
    return new_lst