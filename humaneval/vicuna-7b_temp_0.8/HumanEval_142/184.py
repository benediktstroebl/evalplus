


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
    # Initialize a variable to store the sum of squares
    sum_of_squares = 0
    
    # Check if the list has at least 2 elements
    if len(lst) >= 2:
        # For each element in the list
        for i in range(len(lst)):
            # If the index of the element is a multiple of 3, square the element
            if (i % 3) == 0:
                lst[i] = lst[i]**2
                # Add the squared element to the sum of squares
                sum_of_squares += lst[i]**2
            # If the index of the element is a multiple of 4, cube the element
            elif (i % 4) == 0:
                lst[i] = lst[i]**3
                # Add the cubed element to the sum of squares
                sum_of_squares += lst[i]**3
    
    return sum_of_squares
