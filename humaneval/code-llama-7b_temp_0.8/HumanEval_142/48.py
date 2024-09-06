


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
    # Declare a variable that will hold the sum of the squared and cubed integers
    sum_squared_cubed = 0
    
    # Iterate through the list of integers
    for i in range(len(lst)):
        
        # Check if the index is a multiple of 3 or 4
        if i % 3 == 0 or i % 4 == 0:
            
            # Check if the index is a multiple of 3
            if i % 3 == 0:
                
                # If so, square the integer and add it to the sum
                sum_squared_cubed += lst[i] ** 2
            
            # Check if the index is a multiple of 4
            elif i % 4 == 0:
                
                # If so, cube the integer and add it to the sum
                sum_squared_cubed += lst[i] ** 3
    
    # Return the sum
    return sum_squared_cubed
