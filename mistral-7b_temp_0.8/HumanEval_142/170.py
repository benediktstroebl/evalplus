


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
    # Store the sum of squares in a variable
    sum_square = 0
    # Store the sum of cubes in a variable
    sum_cube = 0
    # Loop through the list
    for i in range(len(lst)):
        # If the index is a multiple of 3, square the integer
        if (i % 3) == 0:
            lst[i] = lst[i] ** 2
        # If the index is a multiple of 4, cube the integer
        elif (i % 4) == 0:
            lst[i] = lst[i] ** 3
        # If the index is a multiple of both 3 and 4, cube the integer
        if (i % 12) == 0:
            lst[i] = lst[i] ** 3
        # Add the squares and cubes to the sum
        sum_square += lst[i]
    # Return the sum
    return sum_square
