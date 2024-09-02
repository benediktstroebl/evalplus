


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
    
    # If the list is not empty and has at least one element
    if len(lst) > 0:
        # Create an empty list to store the sum
        total = []
        
        # Loop through the elements of the list
        for value in lst:
            
            # Check if the index of the value is a multiple of 3
            if (3 * value) % 3 == 0:
                total.append(value ** 2)
            # Check if the index of the value is a multiple of 4
            elif (4 * value) % 4 == 0:
                total.append(value ** 3)
            # Check if the index of the value is not a multiple of 3 or 4
            else:
                total.append(value)
        
        # Return the sum of all entries in the list
        return sum(total)
    # If the list is empty or has no elements
    else:
        return 0