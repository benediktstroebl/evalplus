def is_sorted(lst):
    # Count the unique elements and sort the list if it contains multiple unique elements
    if len(set(lst)) != len(lst):
        lst.sort()    
    # Verify whether the sorted list is consecutive
    for i in range(1, len(lst)):
        if lst[i] - lst[i - 1] > 1: 
            return False
    return True