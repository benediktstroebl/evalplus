


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
    # create a new list to store the squared and cubed values
    new_list = []

    # loop through the list
    for index, value in enumerate(lst):

        # test if the index is a multiple of 3
        if index % 3 == 0:
            # square the value if the index is a multiple of 3
            new_value = value**2
            # append the new value to the new list
            new_list.append(new_value)
        else:
            # just append the original value to the new list
            new_list.append(value)
        
        # test if the index is a multiple of 4
        if index % 4 == 0:
            # cube the value if the index is a multiple of 4
            new_value = value**3
            # append the new value to the new list
            new_list.append(new_value)
        else:
            # just append the original value to the new list
            new_list.append(value)

    # return the sum of the new list
    return sum(new_list)
