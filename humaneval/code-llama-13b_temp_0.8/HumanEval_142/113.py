


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
    
    # 1. iterate through list
    # 2. increment output by value squared if index mod 3 is 0
    # 3. increment output by value cubed if index mod 4 is 0 and not 3
    # 4. return output
    
    output = 0
    
    for index, value in enumerate(lst):
        if index % 3 == 0:
            output += value ** 2
        elif index % 4 == 0 and index % 3 != 0:
            output += value ** 3
            
    return output


    

