


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
    
    # Declaring variables
    # Squares and cubes are lists that will contain the squares and cubes of the list's integers
    squares = []
    cubes = []
    # total will contain the sum of the squares and cubes
    total = 0
    
    # If the list is not empty
    if lst:
        # For every item in the list
        for item in lst:
            # If the item is a multiple of 3
            if item % 3 == 0:
                # Add the squared item to the list of squares
                squares.append(item**2)
            # If the item is a multiple of 4
            if item % 4 == 0:
                # Add the cubed item to the list of cubes
                cubes.append(item**3)
            # If the item is not a multiple of 3 or 4
            else:
                # Add the item to the list of cubes
                cubes.append(item)
        # Return the sum of the squares and cubes
        return sum(squares) + sum(cubes)
        
    # If the list is empty
    else:
        # Return 0
        return 0
