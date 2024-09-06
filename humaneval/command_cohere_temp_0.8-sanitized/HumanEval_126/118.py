def is_sorted(lst):
    # Count the occurrences of each element using a dictionary
    element_count = {}
    for n in lst:
        element_count[n] = element_count.get(n, 0) + 1
    
    # Check for elements being greater than their position indicates
    for i in range(1, len(lst)):
        if lst[i] <= lst[i - 1]:
            return False
    
    # Check for duplicates with count greater than 1
    for n, count in element_count.items():
        if count > 1:
            return False
    
    return True