


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
    
    # create an empty list
    x = []
    # for each item in lst
    for i in range(len(lst)):
        # if the item at index i is a multiple of 3
        if i%3==0:
            # add the square of that item to x
            x.append(lst[i]**2)
        # if the item at index i is a multiple of 4 and not 3
        elif i%4==0:
            # add the cube of that item to x
            x.append(lst[i]**3)
    # return the sum of x
    return sum(x)

