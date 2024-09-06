def strange_sort_list(lst):
    # initialize the minimum and maximum values
    min_ = min(lst)
    max_ = max(lst)
    result = [min_]
    
    # remove the two values from the list
    lst = [x for x in lst if x != min_ and x != max_]
    
    # recursively sort the remaining values
    result += strange_sort_list(lst)
    
    return result + [max_]