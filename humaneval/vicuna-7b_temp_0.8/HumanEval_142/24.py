


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
    # Ensure that all entries in the list are positive integers
    lst = [int(i) for i in lst if i >= 0]
    
    # Initialize the sum of the squares
    sum_of_squares = 0
    
    # Iterate over the list
    for i in range(len(lst)):
        # If the index is a multiple of 3, square the entry
        if (i % 3) == 0:
            lst[i] = lst[i] ** 2
        # If the index is a multiple of 4, cube the entry
        elif (i % 4) == 0:
            lst[i] = lst[i] ** 3
        
        # Add the square or cube of the current entry to the sum of squares
        sum_of_squares += lst[i]
    
    return sum_of_squares
