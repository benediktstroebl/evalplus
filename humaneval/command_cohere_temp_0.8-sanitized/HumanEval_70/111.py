def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_ = min(lst)
    max_ = max(lst)
    
    # Initialize the result list with the initial minimum value
    result = [min_]
    
    while lst:
        # Add the maximum value of the remaining list (excluding the just added min_)
        result.append(max(lst[:-1] if min_ == max_ == lst[-1] else lst))
        
        # Remove the added element from the list
        lst.remove(min_)
        
        # Update the min_ and max_ for the next iteration
        min_, max_ = max_, min_
    
    return result