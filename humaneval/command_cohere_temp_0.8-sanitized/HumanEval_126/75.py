def is_sorted(lst):
    # Count the occurrences of each list element
    occ = {}
    for i in lst:
        occ[i] = occ.get(i, 0) + 1
    
    # Check for duplicates
    for i in occ:
        if occ[i] > 1:
            return False
    
    # Check if occ occurs in sorted order
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))