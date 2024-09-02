


def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """
    # Check if the input is a list
    if not isinstance(lst, list) or not all(isinstance(el, int) for el in lst):
        return 0
    
    # Create a new list to store the result
    result = []
    
    # Iterate over the entries in the input list
    for i, el in enumerate(lst):
        # Check if the index is a multiple of 3
        if i % 3 == 0:
            # Square the entry
            result.append(el**2)
        elif i % 4 == 0:
            # Cube the entry
            result.append(el**3)
        else:
            # Store the entry as is
            result.append(el)
    
    # Return the sum of all entries
    return sum(result)
