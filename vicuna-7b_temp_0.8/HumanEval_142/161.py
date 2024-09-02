


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
    
    # create a new list to store squared/cubed integers
    squared_cubed = []
    # loop through the elements of the list
    for num in lst:
        # check if the index is a multiple of 3
        if num % 3 == 0:
            squared_cubed.append(num**2)
        # check if the index is a multiple of 4
        elif num % 4 == 0:
            squared_cubed.append(num**3)
        else:
            squared_cubed.append(num)
    # adding all the elements of squared_cubed to the original list
    lst += [x for x in squared_cubed]
    # return the sum of all elements
    return sum(lst)

