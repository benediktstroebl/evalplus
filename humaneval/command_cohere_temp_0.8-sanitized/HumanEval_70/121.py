def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_ = min(lst)
    max_ = max(lst)
    result = [min_]
    
    # Iterate through the list, adding the maximum value of the remaining elements to the result, followed by the minimum value of the remaining elements
    for num in lst[1:]:
        if num > max_:
            result.append(max_)
            max_ = num
        else:
            result.append(min_)
            min_ = num
    
    return result