def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_ = min(lst)
    max_ = max(lst)
    
    # Initialize the sorted list
    sorted_lst = [min_]
    
    # Loop through the original list
    for num in lst:
        if num == min_:
            sorted_lst.append(max(lst))
        elif num == max_:
            sorted_lst.append(min(lst))
        else:
            sorted_lst.append(num)
    
    return sorted_lst