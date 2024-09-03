def total_match(lst1, lst2):
    # The lists must have the same length
    if len(lst1) != len(lst2):
        return []
    
    # Initialize a new list to store the result
    result = []
    
    # Loop through the lists and compare characters
    for i in range(len(lst1)):
        if lst1[i] < lst2[i]:
            result.append(lst1[i])
        else:
            result.append(lst2[i])
    
    return result