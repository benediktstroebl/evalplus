def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_ = min(lst)
    max_ = max(lst)
    result = [min_]
    
    # Iterate through the list, alternating between min and max values
    for num in lst:
        if num == min_:
            result.append(max_)
        else:
            result.append(min_)
    return result