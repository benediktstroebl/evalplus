


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
    # the variable to store the result is outside the loop, so it will not be affected by the changes of the list inside the loop
    result = 0
    for i in range(len(lst)):
        # the next line check the index if its a multiple of 3 or 4, if yes the operation is squaring or cubing, if not the operation is 
        # squaring or cubing
        if (i % 3 == 0 or i % 4 == 0):
            # if index is a multiple of 3
            if (i % 3 == 0):
                lst[i] = lst[i]**2
            # if index is a multiple of 4
            elif (i % 4 == 0):
                lst[i] = lst[i]**3
            # change the next operation to avoid that the list is changed in the next iteration
            del lst[i]
        else:
            lst[i] = lst[i]**2
    # the next line checks if the result is not empty and it is a list
    if len(result) > 0 and type(result) == list:
        return sum(result)
    else:
        return result

