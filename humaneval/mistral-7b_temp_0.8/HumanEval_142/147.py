


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
    # set up the list that will be the output for the function
    result_lst = []

    # iterate over each index of the input list
    for index, entry in enumerate(lst):

        # if index is a multiple of 3 then square
        if index % 3 == 0:
            result_lst.append(entry ** 2)

        # if index is a multiple of 4 and not a multiple of 3 then cube
        elif index % 4 == 0:
            result_lst.append(entry ** 3)

        # append the entry as is if not a multiple of 3 or 4
        else:
            result_lst.append(entry)

    # sum the list
    return sum(result_lst)

