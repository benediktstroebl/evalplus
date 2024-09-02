


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

    # initialize the new list to hold the entries that will be added
    lst_sum = []

    # iterate through the input list
    for i in range(len(lst)):
        # check if the index is a multiple of 3 or a multiple of 4 but not a multiple of 3
        if (i % 3 == 0 or i % 4 == 0) and i % 3!= 0:
            # square the entry if the index is a multiple of 3
            lst_sum.append(lst[i] ** 2)
        # if the index is not a multiple of 3 or 4
        else:
            # append the entry to the list to be summed
            lst_sum.append(lst[i])

    # return the sum of all entries in the new list
    return sum(lst_sum)

