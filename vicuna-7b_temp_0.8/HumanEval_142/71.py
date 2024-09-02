


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
    # Check if the length of the list is zero
    if len(lst) == 0:
        return 0
    
    # Check if the length of the list is odd
    if len(lst) % 2 == 0:
        return sum(lst)**2
    else:
        # Initialize a variable for storing the sum
        sum = 0
        # Iterate through the list
        for i in range(len(lst)):
            # If the index is a multiple of 3, square the value
            if lst[i] % 3 == 0:
                sum += lst[i]**2
            # If the index is a multiple of 4, cube the value
            elif lst[i] % 4 == 0:
                sum += lst[i]**3
            # If the index is not a multiple of 3 or 4, do not change the value
            else:
                pass
            pass
        return sum