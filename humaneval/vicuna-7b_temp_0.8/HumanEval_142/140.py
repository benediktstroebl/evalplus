


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
    # Check if the list is empty or not
    if not lst:
        return 0
    
    # Create a new list to store the modified values
    modified_lst = []
    
    # Iterate through the original list
    for i in range(len(lst)):
        
        # If the index is a multiple of 3, square the value, else cube it
        if (i % 3) == 0:
            modified_lst.append(lst[i]**2)
        else:
            modified_lst.append(lst[i]**3)
            
    # Append the original values to the new list
    modified_lst.append(lst)
    
    # Return the sum of all values in the modified list
    return sum(modified_lst)