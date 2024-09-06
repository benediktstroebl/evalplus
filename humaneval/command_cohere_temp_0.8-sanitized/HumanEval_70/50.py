def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_ = lst[0]
    max_ = lst[0]
    
    # Sort the list in the "strange" way
    for num in lst[1:]:
        if num > max_:
            max_ = num
        elif num < min_:
            min_ = num
    
    return [min_, max, min_, max_] + [num for num in lst if num > max and num < min_]