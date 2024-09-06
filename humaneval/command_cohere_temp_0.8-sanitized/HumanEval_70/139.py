def strange_sort_list(lst):
    # Create a temporary list to store the sorted values
    res = []

    # Sort the list based on the criteria mentioned in the prompt
    for i in range(len(lst)):
        # Append the smallest value to the result
        res.append(min(lst[i:]))
        # Remove the smallest value from the remaining list
        lst = lst[i+1:]
        # If the list is empty, break the loop
        if not lst:
            break
    # Append the largest value to the result
    res.append(max(lst))
    return res