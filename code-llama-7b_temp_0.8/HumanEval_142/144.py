


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
    
    # Perform a for loop to iterate through the list
    for idx, entry in enumerate(lst):
        
        # If the index is divisible by 3, add the squared value to the running total
        if idx % 3 == 0:
            entry **= 2
        
        # If the index is divisible by 4, add the cubed value to the running total
        elif idx % 4 == 0:
            entry **= 3
        
        # If the index is not divisible by 3 or 4, add the original entry to the running total
        else:
            pass
        
        # Add the value of the current list entry to the running total
        lst[idx] = entry
    
    # Return the value of the running total
    return sum(lst)

