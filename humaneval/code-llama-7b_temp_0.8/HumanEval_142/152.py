


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

    #Check if list is empty
    if lst == []:
        return 0

    #List to store the calculated entries
    lst_updated = []

    for idx, val in enumerate(lst):

        #If the index is a multiple of 3, square the integer
        if idx%3 == 0:
            lst_updated.append(val**2)
        #If the index is a multiple of 4 but not of 3, cube the integer
        elif idx%4 == 0:
            lst_updated.append(val**3)
        #Otherwise keep the original value
        else:
            lst_updated.append(val)

    return sum(lst_updated)

