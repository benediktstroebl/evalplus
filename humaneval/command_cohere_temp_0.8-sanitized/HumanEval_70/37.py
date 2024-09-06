def strange_sort_list(lst):
    # Define a variable to store the minimum value as we iterate through the list
    min_val = float('inf')
    # Initialize the res list with the minimum value of the list
    res = [x for x in lst if x < min_val]
    # Reset min_val to the maximum value of the remaining elements in the list
    min_val = float('-inf')
    for x in lst:
        if x > min_val:
            res.append(x)
            min_val = x
    # If there are remaining elements in the list, add them to the end of res
    if min_val < float('inf'):
        res.extend([x for x in lst if x == min_val])
    return res