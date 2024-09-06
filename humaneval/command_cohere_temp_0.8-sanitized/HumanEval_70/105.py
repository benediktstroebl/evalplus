def strange_sort_list(lst):
    # Initialize the minimum and maximum values
    min_ = lst[0]
    max_ = lst[0]
    
    # Sort the list alternatively using the minimum and maximum values
    for n in lst:
        if n < min_:
            min_ = n
        elif n > max_:
            max_ = n
    
    return [min_, max_, min_, max_] * (len(lst) // 2) + [min_, max_] * (len(lst) % 2)