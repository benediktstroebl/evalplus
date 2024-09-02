


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
    # Check if there are any non zero elements in the list
    if any(lst):
        # Initialize a variable to store the sum
        sum = 0
        # Iterate over the list using a for loop
        for x in lst:
            if x % 3 == 0:
                # If the index is a multiple of 3, square the value
                sum += x**2
            elif x % 4 == 0:
                # If the index is a multiple of 4, cube the value
                sum += x**3
            else:
                # If the index is not a multiple of 3 or 4, do not change the value
                sum += x
    else:
        # Return 0 if the list is empty
        return 0
    return sum

