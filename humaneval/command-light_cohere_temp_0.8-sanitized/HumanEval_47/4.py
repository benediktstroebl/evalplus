def median(lst):
    """Return the median of the list lst."""
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    
    # Check if the length of the list is even
    if n % 2 == 0:
        mid = (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2
    else:
        mid = sorted_lst[n // 2]
    
    return mid