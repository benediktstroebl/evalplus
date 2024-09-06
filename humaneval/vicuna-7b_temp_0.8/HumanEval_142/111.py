


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
    
    # a list of booleans that track if the index is a multiple of 3
    is_3_multiple = [True]*len(lst)
    # a list of booleans that track if the index is a multiple of 4
    is_4_multiple = [False]*len(lst)
    
    # initialize a list to store the squared and cubed values
    squared_and_cubed = [lst[i]*i for i in range(1, len(lst)+1)]
    # initialize a variable to store the sum of squares
    result = 0
    
    # loop through the list
    for i in range(len(lst)):
        # if the index is a multiple of 3, square it, otherwise cube it
        if i % 3 == 0:
            squared_and_cubed[i] = lst[i]**2
        else:
            squared_and_cubed[i] = lst[i]**3
        
        # add the squared and cubed values to the result
        result += squared_and_cubed[i]
    
    # return the result
    return result

