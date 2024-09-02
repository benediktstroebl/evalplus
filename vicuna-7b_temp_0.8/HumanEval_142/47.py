


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
    
    # Create an empty list to store the intermediate results
    intermediate = []
    
    # Loop through the list
    for num in lst:
        # Check if the index is a multiple of 3
        if num % 3 == 0:
            intermediate.append(num ** 2)
        # Check if the index is a multiple of 4
        elif num % 4 == 0:
            intermediate.append(num ** 3)
        else:
            intermediate.append(num ** 2)
    
    # Return the sum of all intermediate results
    return sum(intermediate)
