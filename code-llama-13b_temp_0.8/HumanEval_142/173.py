


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
    
    # Initialize the total
    total = 0
    
    # Set a counter to keep track of the index
    i = 0
    
    # Loop through all elements
    for item in lst:
        # If the index is a multiple of 3, square the number
        if i % 3 == 0:
            item = item ** 2
            
        # If the index is a multiple of 4, cube the number
        if i % 4 == 0 and i % 3 != 0:
            item = item ** 3
            
        # Add to the total
        total += item
        
        # Increment the index
        i += 1
        
    # Return the total
    return total

