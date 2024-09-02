


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
    # initialize the sum of the squared values
    sum_sq = 0
    
    # loop through the list, incrementing the sum for each value
    for i,n in enumerate(lst):
        # calculate the value to be added to the sum
        value = n**2 if (i+1) % 3 == 0 else n**3 if (i+1) % 4 == 0 else 0
        # add the value to the sum
        sum_sq += value
    return sum_sq

