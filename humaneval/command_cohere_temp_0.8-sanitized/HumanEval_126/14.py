def is_sorted(lst):
    # Count the occurrences of each element using a dictionary
    element_count = {}
    for element in lst:
        element_count[element] = element_count.get(element, 0) + 1
    
    # Check for elements being greater than their preceding elements
    for i in range(1, len(lst)):
        if lst[i] <= lst[i - 1]:
            return False
    
    # Check for more than one occurrence of the same number
    for element, count in element_count.items():
        if count > 1:
            return False
    
    return True