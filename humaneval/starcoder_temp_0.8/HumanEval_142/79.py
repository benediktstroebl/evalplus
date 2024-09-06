


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

    # create new list to store values to sum
    new_lst = []
    
    # for each entry in lst, append value to new_lst
    for index in range(len(lst)):
        if (index % 3 == 0) and (index % 4!= 0):
            # if the index is a multiple of 3 and not a multiple of 4, square the value
            new_lst.append(lst[index] ** 2)
        elif (index % 3!= 0) and (index % 4 == 0):
            # if the index is a multiple of 4 and not a multiple of 3, cube the value
            new_lst.append(lst[index] ** 3)
        else:
            # else append the value without modifying
            new_lst.append(lst[index])

    # return the sum of all values in the new list
    return sum(new_lst)
