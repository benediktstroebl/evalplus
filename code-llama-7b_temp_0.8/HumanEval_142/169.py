


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
    
    # create a variable to store the sum of the cubes
    sum_cubes = 0
    
    # create a variable to store the sum of the squares
    sum_squares = 0
    
    # iterate through the list of integers
    for i, integer in enumerate(lst):
        # if the index is a multiple of 4 and not a multiple of 3
        if i % 4 == 0 and i % 3 != 0:
            # add the integer to the sum_cubes
            sum_cubes += int(integer**3)
        # if the index is a multiple of 3
        elif i % 3 == 0:
            # add the integer to the sum_squares
            sum_squares += int(integer**2)
            
    # return the sum of the cubes and squares
    return sum_cubes + sum_squares


