


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
    # Setting up a variable to store the sum of the squares
    total = 0

    # iterating through the list
    for idx, item in enumerate(lst):
        # if the index is a multiple of 3, we square the entry in the list
        if idx % 3 == 0:
            total += item ** 2
        # if the index is a multiple of 4 and not a multiple of 3, we cube the entry in the list
        elif idx % 4 == 0:
            total += item ** 3
    return total
