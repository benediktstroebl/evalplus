


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
    
    # initialize an empty list
    # store the output of the function in this list
    # for all entries in the input list
    #   if the index is a multiple of 3 or 4
    #       square the entry if the index is a multiple of 3
    #       cube the entry if the index is a multiple of 4
    #   else
    #       do not change the entry
    #   add the entry to the output list

    # initialize an empty list
    # for every element in the input list
    #   if the index is a multiple of 3 or 4
    #       square the element if the index is a multiple of 3
    #       cube the element if the index is a multiple of 4
    #   else
    #       do not change the element
    #   add the element to the output list
    # return the sum of the output list
    
    # initialize an empty list
    new_lst = []
    for index, element in enumerate(lst):
        if index % 3 == 0:
            element *= element
        elif index % 4 == 0:
            element *= element * element
        new_lst.append(element)
    return sum(new_lst)
