def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_ = lst[0]
    max_ = lst[0]
    
    # Loop to find the maximum and minimum values in the list
    for n in lst[1:]:
        if n > max_:
            max_ = n
        elif n < min_:
            min_ = n
    
    # Return the sorted list in the required format
    return [min_, max_, *sorted(lst)[1:-1]]