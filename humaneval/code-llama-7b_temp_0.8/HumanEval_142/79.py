


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

    """
    This is my solution
    """
    # make a copy of the list 
    working_lst = lst.copy()
    # set the sum to zero
    sum_of_squares = 0
    # loop through each index
    for i in range(len(working_lst)):
        # if the index is a multiple of 3
        if i%3 == 0:
            # then square the value at that index
            working_lst[i] = working_lst[i]**2
        # if the index is a multiple of 4 
        if i%4 == 0:
            # and not a multiple of 3
            if i%3 != 0:
                # then cube the value at that index
                working_lst[i] = working_lst[i]**3
        # add the value at that index to the sum
        sum_of_squares = sum_of_squares + working_lst[i]
    # return the sum of the values squared
    return sum_of_squares




