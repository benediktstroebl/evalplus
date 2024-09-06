


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
    # Initialize the sum of squares to zero
    sum_of_squares = 0
    
    # Loop through all the entries in the list
    for i in range(len(lst)):
        # If the index is a multiple of 3, square the value
        if (i % 3 == 0):
            lst[i] = lst[i] ** 2
        # If the index is a multiple of 4, cube the value
        elif (i % 4 == 0):
            lst[i] = lst[i] ** 3
        # Otherwise, do not change the value
        else:
            pass
        
    # Sum of squares is the sum of all the entries in the list
    return sum(lst)


