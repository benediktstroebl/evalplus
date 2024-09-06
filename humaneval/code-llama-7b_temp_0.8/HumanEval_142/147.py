


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
    
    # a list to store the squared numbers
    squared_numbers = []
    
    # a list to store the cubed numbers
    cubed_numbers = []
    
    # iterate over lst
    for index, item in enumerate(lst):
        
        # check if index is a multiple of 3
        if index % 3 == 0:
            
            # if it is, square item and store in squared_numbers
            squared_numbers.append(item ** 2)
            
        # check if index is a multiple of 4 and not a multiple of 3
        elif index % 4 == 0 and index % 3 != 0:
            
            # if it is, cube item and store in cubed_numbers
            cubed_numbers.append(item ** 3)
            
        else:
            
            # if it is not, add item to squared_numbers
            squared_numbers.append(item)
            
    # add the sum of squared_numbers and cubed_numbers
    return sum(squared_numbers) + sum(cubed_numbers)








