


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
    # Check for emptiness of the list
    if not lst:
        return 0
    
    # Initialize a variable to store the sum
    sum = 0
    
    # Loop through the list
    for num in lst:
        # Check if the index is a multiple of 3 or 4
        if (num % 3 == 0 or num % 4 == 0):
            # Square the number if it is a multiple of 3, cube it if it is a multiple of 4
            if (num % 3 == 0):
                num = num ** 2
            elif (num % 4 == 0):
                num = num ** 3
            # Add the number to the sum
            sum += num
    
    # Return the sum
    return sum

