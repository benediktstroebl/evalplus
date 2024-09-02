


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
    
    # Check if the list is empty
    if not lst:
        return 0
    
    # Initialize a variable to store the current sum
    current_sum = 0
    
    # Iterate over the list
    for element in lst:
        
        # Check if the index of the element is a multiple of 3
        if (element % 3 == 0):
            current_sum += element ** 2
        else:
            # Check if the index of the element is a multiple of 4
            if (element % 4 == 0):
                current_sum += element ** 3
            else:
                current_sum += element ** 2
    
    return current_sum
