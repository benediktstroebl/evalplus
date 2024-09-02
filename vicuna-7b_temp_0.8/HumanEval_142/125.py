


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
    # sort the list by indexing the list with a slice, this sorts the list in place
    lst.sort()
    
    # initialize a variable to store the sum of the squares
    sum = 0
    
    # iterate over the list, squaring or cubing the integers as appropriate
    for i in range(len(lst)):
        if (i % 3 == 0) or (i % 4 == 0):
            # if the index is a multiple of 3 or 4, then square the integer
            lst[i] = lst[i] ** 2
        else:
            # if the index is not a multiple of 3 or 4, then cube the integer
            lst[i] = lst[i] ** 3
    
    # add the squares or cubes to the sum
    for i in range(len(lst)):
        sum += lst[i]
    
    return sum

