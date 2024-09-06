


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
    # convert the list to a list of lists
    lst = [lst]
    
    for x in lst:
        # initialize a variable to store the current sum
        current_sum = 0
        
        # check if the list is empty
        if not x:
            return 0
        
        # check if the list is empty
        if len(x) == 0:
            return 0
        
        for i in range(len(x)):
            # check if the current index is a multiple of 3
            if i % 3 == 0:
                # square the current element
                x[i] = x[i]**2
            # check if the current index is a multiple of 4
            elif i % 4 == 0:
                # cube the current element
                x[i] = x[i]**3
            else:
                # keep the element as is
                current_sum += x[i]
        
        # return the sum of all elements
        return current_sum
