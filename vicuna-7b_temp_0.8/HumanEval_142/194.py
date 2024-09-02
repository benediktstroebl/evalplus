


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
    # check if the list is empty
    if not lst:
        return 0
    
    # get the length of the list
    len_lst = len(lst)
    
    # check if the list is empty
    if len_lst == 0:
        return 0
    
    # initialize the sum to 0
    sum = 0
    
    # iterate over the elements in the list
    for i in range(len_lst):
        # check if the index is a multiple of 3
        if i % 3 == 0:
            # square the number
            sum += lst[i] ** 2
        elif i % 4 == 0:
            # cube the number
            sum += lst[i] ** 3
        else:
            # add the number to the sum
            sum += lst[i]
            
    return sum
